#!/usr/bin/env python3
"""
module that writes strings to redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    a class called cache to write redis strings.
    """
    def __init__(self):
        """
        Initiating variables.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        a methods thats takes data as an arguements
        returns a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

