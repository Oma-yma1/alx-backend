#!/usr/bin/env python3
"""jjkkll"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """llllll"""

    def __init__(self) -> None:
        """ooooo"""
        super().__init__()

    def put(self, key, item):
        """kkkkk"""
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            del self.cache_data[key]
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data.keys())[-2]
            print("DISCARD: {}".format(first_key))
            del self.cache_data[first_key]

    def get(self, key):
        """llll"""
        if key is None or key not in self.cache_data.keys():
            return None
