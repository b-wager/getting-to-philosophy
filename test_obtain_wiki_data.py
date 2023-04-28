"""
Tests for the obtain_wiki_data module

The unit tests are slow so I tried to test functions
dependent on other functions as well as condense multiple
tests into one to save time
"""

import wikipedia
from obtain_wiki_data import random_page, create_link_list, network_step, get_links

def test_random_page_returns_a_page():
    """
    Tests that the random_page function correctly returns a
    WikipediaPage object.
    """
    assert isinstance(random_page(), wikipedia.wikipedia.WikipediaPage)


def test_create_link_list_output_max_size():
    """
    Tests the create_link_list function correctly returns a
    list of links of no greater than the desired size
    """
    assert len(create_link_list(8,10)) <= 80


def test_create_link_list_output_min_size():
    """
    Tests the create_link_list function correctly returns a
    list of links of a reasonable size.
    """
    assert len(create_link_list(8,10)) >= 40

def test_network_step():
    """
    Tests the network_step if it returns
    reasonable data under normal conditon
    """
    return_dict = {}
    network_step(5, 2, return_dict)
    assert len(return_dict[2]) <= 5


def test_get_links():
    """
    Tests get_links, a wrapper that lets us
    easily spawn individual workers based on
    random_page() that loop for a given depth
    """
    return_dict = {}
    get_links(1, 5, return_dict)
    assert len(return_dict) <= 5
