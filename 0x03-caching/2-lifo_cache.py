#!/usr/bin/env python3
"""Module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Docstring placeholder
    """

    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """ Adds"""
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
           and key not in self.cache_data.keys():
            to_remove = list(self.cache_data.keys())[
                BaseCaching.MAX_ITEMS - 1]
            del self.cache_data[to_remove]
            print("DISCARD: {}".format(to_remove))
        if(key in self.cache_data.keys()):
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        """ Gets """
        if(key is None or key not in self.cache_data.keys()):
            return
        return self.cache_data.get(key)
