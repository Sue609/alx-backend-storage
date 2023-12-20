#!/usr/bin/env python3
"""
module that writes strings to redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator function for coounting how many times
    the methods of the class are called.
    """

    @wraps(method)
    def wrappers(self, *args, **kwargs):
        """
        wrapper function
        """
        key = method.__qualname__
        self.redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Reading from redis and recovering original type.
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        uses the get method with a lambda function to decode
        the retrieved data as UTF-8 and returns it as a string or
        None if the key does not exist.
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        uses the get method with a lambda function to convert the
        retrieved data to an integer or None if the key does not exist.
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value

