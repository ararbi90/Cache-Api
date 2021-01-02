"""
Module contains CacheSet class
"""
from .cache import Cache
from .cache_factory import CacheFactory

class CacheSet:
    """
    Class used to store cache based on user
    """
    def __init__(self, size: int):
        """
        @param size of each cache
        """ 
        self.size = size
        self.cacheSet = {}

    def add(self, user: str, key, value):
        """
        Add cache based on user and key
        @param user: user name assocaited with cache
        @param key: key for cache object
        @param value: value of cache object
        """
        if user not in self.cacheSet:
            self.cacheSet[user] = Cache(self.size, CacheFactory.LRU)
        self.cacheSet[user].add(key, value)

    def get(self, user: str, key):
        """
        Get cache value based on user and key
        @param user: user associated with cache
        @param key: key associated with cache
        @return value associated with cache
        """
        if user in self.cacheSet:
            return self.cacheSet[user].get(key)
        return None