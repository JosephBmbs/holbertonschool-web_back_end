#!/usr/bin/env python3
"""A type-annotated function make_multiplier that takes a float multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return callable function: miltiplies a float by multiplier variable """

    return lambda x: x * multiplier
