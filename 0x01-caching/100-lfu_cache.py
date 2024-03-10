#!/usr/bin/env python3
"""Implementing a LFU caching system."""

from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching system inheriting from BaseCaching."""

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If key already exists, increase its frequency
            self.frequency[key] += 1
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the least frequency used item (LFU)
            min_frequency = min(self.frequency.values())
            least_frequent_keys = [k for k, v in self.frequency.items() if v == min_frequency]
            if len(least_frequent_keys) == 1:
                lfu_key = least_frequent_keys[0]
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                print("DISCARD:", lfu_key)
            else:
                # Use LRU algorithm to discard only the least recently used
                lru_key = min(least_frequent_keys, key=lambda k: self.cache_data[k])
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.frequency[key] += 1

    def get(self, key):
        """Get an item from the cache."""
        if key is None:
            return None
        if key in self.cache_data:
            # Increase frequency and return item
            self.frequency[key] += 1
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    lfu_cache = LFUCache()
