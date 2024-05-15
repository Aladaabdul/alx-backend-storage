#!/usr/bin/env python3


"""working with redis"""


import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the count and calls the original method.
        """
        # Generate the key using the method's qualified name
        key = f"{method.__qualname__}_calls"
        # Increment the count in Redis
        self._redis.incr(key)
        # Call the original method
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """Class Cache implementation

    """
    def __init__(self):
        """Initialize the redis client

        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes a data argument
        and return a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str,
            bytes,
            int,
            float,
            None
            ]:
        """get method that take a key string argument
        and an optional Callable argument named fn
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """get_str function
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """get_int function
        """
        return self.get(key, lambda d: int(d))
