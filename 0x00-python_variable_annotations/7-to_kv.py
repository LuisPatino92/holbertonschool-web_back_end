#!/usr/bin/env python3
"""Function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Makes a conversion
    """
    return (k, v ** 2)
