"""
Contains interface for cache algorithm
"""
from abc import ABC, abstractmethod

class ICache(ABC):

    @property
    @abstractmethod
    def add(self, key):
        """
        Add a key to the cache algorithm 
        @param key of the chace
        @return key if needs to be deleted. 
        """
        pass


