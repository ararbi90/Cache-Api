"""
"""
class Node:
    """
    """
    def __init__(self, key):
        """
        @param key of the node
        """
        self.key = key
        self.next = None
        self.prev = None

    def __str__(self):
        return f"key: {self.key}"

    def __repr__(self):
        return f"key: {self.key}" 