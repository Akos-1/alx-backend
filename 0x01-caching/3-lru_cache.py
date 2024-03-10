#!/usr/bin/env python3
"""Implementing a LRU caching system."""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system inheriting from BaseCaching."""

    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If key already exists, move it to the end of the queue
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the least recently used item (LRU)
            lru_key = self.queue.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """Get an item from the cache."""
        if key is None:
            return None
        if key in self.cache_data:
            # Move accessed item to the end of the queue
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    lru_cache = LRUCache()
