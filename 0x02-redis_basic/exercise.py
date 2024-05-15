#!/usr/bin/env python3


"""working with redis"""


import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    """Class Cache implementation

    """
    def __init__(self):
        """Initialize the redis client

        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
        data = self._radis.get(key)
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
