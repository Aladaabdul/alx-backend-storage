#!/usr/bin/env python3


"""working with redis"""


import redis
import uuid
from typing import Union


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
