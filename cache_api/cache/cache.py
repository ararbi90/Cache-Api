"""
"""
from .cache_factory import CacheFactory
from .icache import ICache

class Cache:
    """
    """
    def __init__(self, capacity: int, algo: str):
        """
        """
        self._algo = CacheFactory.getCache(algo, capacity)
        self._map = {}

    def add(self, key, value):
        """
        """
        self._map[key] = value
        evict = self._algo.add(key)
        if evict:
            del self._map[evict]
    
    def get(self, key):
        """
        """
        self._algo.add(key)
        return self._map.get(key, None)

    def __repr__(self):
        return str(self._map)




