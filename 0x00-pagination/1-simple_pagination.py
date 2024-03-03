#!/usr/bin/env python3

"""
This module provides a function and a
class to handle pagination of a dataset.
"""

import csv
from typing import List
import math


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of the dataset based on pagination parameters.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of items per page.
            Defaults to 10.

        Returns:
            List[List]: The list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,

        dataset_length = len(self.dataset())
        total_pages = math.ceil(dataset_length / page_size)

        if page > total_pages:
            return []

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index + 1]


# Example usage
if __name__ == "__main__":
    server = Server()

    # Test get_page method
    page_number = 3
    items_per_page = 10
    page_data = server.get_page(page_number, items_per_page)
    print(f"Page {page_number} data:")
    for row in page_data:
        print(row)
