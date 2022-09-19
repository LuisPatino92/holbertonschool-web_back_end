#!/usr/bin/env python3
"""Function"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list"""
    return [(x, len(x)) for x in lst]
