#!/usr/bin/env python3
"""
module that writes strings to redis
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        """
        Reading from redis and recovering original type.
        """
        value = self._redis.get(Key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """
        uses the get method with a lambda function to decode
        the retrieved data as UTF-8 and returns it as a string or
        None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """
        uses the get method with a lambda function to convert the
        retrieved data to an integer or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: int(d))

