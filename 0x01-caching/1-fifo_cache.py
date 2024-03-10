#!/usr/bin/env python3
"""Implementing a FIFO caching system."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system inheriting from BaseCaching."""

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the first item (FIFO)
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache."""
        if key is None:
            return None
        return self.cache_data.get(key)


if __name__ == "__main__":
    fifo_cache = FIFOCache()
