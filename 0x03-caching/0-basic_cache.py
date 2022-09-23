#!/usr/bin/env python3
"""Module that has a more wide description """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Docstring placeholder
    This is a pretty functuion
    """

    def put(self, key, item):
        """ Adds to cache in a basic way"""
        if item is None or key is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Ggets from cache  in basic way"""
        if key is None or key not in self.cache_data.keys():
            return
        else:
            return self.cache_data.get(key)
