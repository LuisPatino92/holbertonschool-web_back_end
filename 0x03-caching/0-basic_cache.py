#!/usr/bin/env python3
"""Module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Docstring placeholder
    """

    def put(self, key, item):
        """ Adds to cache"""

        if item is None or key is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Ggets from cache """

        if key is None or key not in self.cache_data.keys():
            return
        else:
            return self.cache_data.get(key)
