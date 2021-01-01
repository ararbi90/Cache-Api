from lru_cache import Lru
from mru_cache import Mru
from cache_set import CacheSet

if __name__ == "__main__":
    set = CacheSet(3)
    set.add("ahmed", 1, 1)
    print(set.cacheSet)
    set.add("ahmed", 2, 2)
    print(set.cacheSet)
    set.add("ahmed", 3, 3)
    print(set.cacheSet)
    set.get("ahmed", 1)
    print(set.cacheSet)
    set.add("ahmed", 4, 4)
    print(set.cacheSet)
    print(set.get("sam", 1))
