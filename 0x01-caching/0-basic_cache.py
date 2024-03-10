#!/usr/bin/env python3
"""Implementing a basic caching system."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system inheriting from BaseCaching."""

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache."""
        if key is None:
            return None
        return self.cache_data.get(key)


if __name__ == "__main__":
    basic_cache = BasicCache()
