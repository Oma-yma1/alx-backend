#!/usr/bin/python3
"""task 5 lfucahing"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """class LFUcache"""

    def __init__(self):
        """init object"""
        super().__init__()
        self.uses = dict()

    def put(self, key, item):
        """function put"""
        if(key is None or item is None):
            return

        if(len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
           and key not in self.cache_data.keys()):
            discard_key = min(self.uses, key=self.uses.get)
            del self.cache_data[discard_key]
            del self.uses[discard_key]
            print("DISCARD: {}".format(discard_key))
        if(key in self.cache_data.keys()):
            self.uses[key] += 1
        else:
            self.uses[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """function get"""
        if(key is None or key not in self.cache_data.keys()):
            return
        self.uses[key] += 1
        return self.cache_data.get(key)
