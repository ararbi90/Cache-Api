"""
Module contains factory for caching algorithm
"""
from .icache import ICache
from .lru_cache import Lru
from .mru_cache import Mru

class CacheFactory:
    """
    Factory provides a caching algorithm
    """
    LRU = "LRU"
    MRU = "MRU"

    @staticmethod
    def getCache(cache: str, capacity: int) -> ICache:
        """
        @param cache type of cache algorithm
        @param capacity for cache
        @return ICache algorithm
        """
        if cache == CacheFactory.LRU:
            return Lru(capacity)
        else:
            return Mru(capacity)