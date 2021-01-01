"""
"""
from .icache import ICache
from .lru_cache import Lru
from .mru_cache import Mru

class CacheFactory:
    """
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