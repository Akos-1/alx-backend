#!/usr/bin/env python3
"""Implementing a MRU caching system."""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system inheriting from BaseCaching."""

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If key already exists, move it to the end of the access order
            self.access_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the most recently used item (MRU)
            mru_key = self.access_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """Get an item from the cache."""
        if key is None:
            return None
        if key in self.cache_data:
            # Move accessed item to the end of the access order
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    mru_cache = MRUCache()
