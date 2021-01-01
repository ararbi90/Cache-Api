"""
"""
from .cache import Cache
from .cache_factory import CacheFactory

class CacheSet:
    """
    @param size of each cache
    """  
    def __init__(self, size: int):
        self.size = size
        self.cacheSet = {}

    def add(self, user: str, key, value):
        if user not in self.cacheSet:
            self.cacheSet[user] = Cache(self.size, CacheFactory.LRU)
        self.cacheSet[user].add(key, value)

    def get(self, user: str, key):
        if user in self.cacheSet:
            return self.cacheSet[user].get(key)
        return None