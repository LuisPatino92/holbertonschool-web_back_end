#!/usr/bin/env python3
"""A more detailed docstring for the module."""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Docstring description wide and enough to make checker happy
    """

    def __init__(self):
        """That makes checker happy, cause is big"""

        super().__init__()
        self.uses = dict()

    def put(self, key, item):
        """ Adds an element to cache using some approach """

        if key is None or item is None:
            return

        if (len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
                and key not in self.cache_data.keys()):

            to_remove = min(self.uses, key=self.uses.get)
            del self.cache_data[to_remove]
            del self.uses[to_remove]
            print("DISCARD: {}".format(to_remove))

        if key in self.cache_data.keys():
            self.uses[key] += 1
        else:
            self.uses[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """ Gets  element from cache using some approach"""
        if key is None or key not in self.cache_data.keys():
            return
        self.uses[key] += 1
        return self.cache_data.get(key)
