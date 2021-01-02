"""
Module contains Cache object
"""
from .cache_factory import CacheFactory
from .icache import ICache

class Cache:
    """
    Implementation of a cache. Takes a size and cache algorithm in as input
    """
    def __init__(self, capacity: int, algo: str):
        """
        @param capacity: size of cache
        @param algo: agorithm for cache
        """
        self._algo = CacheFactory.getCache(algo, capacity)
        self._map = {}

    def add(self, key, value):
        """
        Add key and value to cache
        @param key: key assocaited with cache
        @param value: value associated with cache
        """
        self._map[key] = value
        evict = self._algo.add(key)
        if evict:
            del self._map[evict]
    
    def get(self, key):
        """
        Get value from cache
        @param key: key assocaited with cache
        @return value associated with cache
        """
        self._algo.add(key)
        return self._map.get(key, None)

    def __repr__(self):
        return str(self._map)




