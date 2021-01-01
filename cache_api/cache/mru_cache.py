"""
 Contains Mru cache implementation
"""
from .icache import ICache
from .cache_node import Node

class Mru(ICache):
    """
    Implementation of LRU cache
    """
    def __init__(self, capacity: int):
        """
        @param capacity of the cache
        """
        self.capacity = capacity
        self.map = {}
        self.head = Node(None)
        self.tail = Node(None)
        self.tail.prev = self.head
        self.head.next = self.tail

    def add(self, key):
        """
        Add a key to the cache algorithm 
        @param key of the chace
        @return key if needs to be deleted. 
        """
        current = self.map[key] if key in self.map else None
        node = None
        
        if current == None:
            node = Node(key)
            self.map[key] = node
        else:
            node = self.map[key]

        # Check for eviction
        evictionKey = None
        if(len(self.map) > self.capacity):
            temp = self.head.next
            self.head.next = temp.next
            temp.next.prev = self.head
            temp.prev = None
            temp.next = None
            evictionKey = temp.key

        # Update status
        if node.next and node.prev:
            node.next.prev = node.prev
            node.prev.next = node.next

        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

        if evictionKey:
            del self.map[evictionKey]

        return evictionKey   

        
        

