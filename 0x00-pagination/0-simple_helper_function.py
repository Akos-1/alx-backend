#!/usr/bin/env python3

"""
This module provides a function to calculate
the start and end indices for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indices for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and
        end indices for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index


# Example usage
if __name__ == "__main__":
    page_number = 3
    items_per_page = 10
    start, end = index_range(page_number, items_per_page)
    print(f"Start index: {start}, End index: {end}")
