#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size  two a start index and end index"""
    return ((page - 1) * page_size, page * page_size)
