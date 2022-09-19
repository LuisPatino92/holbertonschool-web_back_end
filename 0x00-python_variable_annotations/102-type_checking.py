#!/usr/bin/env python3
"""Function"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """List"""
    zoomed: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed:


if __name__ == "__main__":
    array = tuple([12, 72, 91])
    zoom_2x = zoom_array(array)
    zoom_3x = zoom_array(array, int(3.0))
