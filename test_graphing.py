"""
Tests for the graphing modules.
Many functions are visual with no returns
so they were not unit tested.

The unit tests are slow so I tried to test functions
dependent on other functions as well as condense multiple
tests into one to save time
"""

import graphing
import follow_first_link
import obtain_wiki_data


def test_generate_edges():
    """
    Tests if generate_edges returns the proper type
    which is a list of 2-length tuples 
    """
    edges = graphing.generate_edges([1, 2, 3, 4, 5])
    assert edges[0] == (1, 2) and edges[1] == (2, 3)

def test_get_paths_first_links():
    """
    Tests if get_paths runs and returns the proper format
    which is a list of lists where the outer list has length
    less than or equal to the threadcount (20) and the inner
    lists have length less than or equal to the depth + 1 (6)
    Error handling is done just by letting branches die, so
    it is possible and expected for some branches or
    occassionally entire workers to die but this is rare.

    This version sees if get_paths correctly executes workers
    for find_first_links.
    """
    paths_first = graphing.get_paths(5, 20, follow_first_link.find_first_link)
    print("first setup")
    assert len(paths_first) <= 6 and len(paths_first[0]) <= 21

def test_get_paths_network_step():
    """
    Tests if get_paths runs and returns the proper format
    which is a list of lists where the outer list has length
    less than or equal to the threadcount (20) and the inner
    lists have length less than or equal to the depth + 1 (6)
    Error handling is done just by letting branches die, so
    it is possible and expected for some branches or
    occassionally entire workers to die but this is rare.

    This version sees if get_paths correctly executes workers
    for network_step
    """
    paths_random = graphing.get_paths(5, 20, obtain_wiki_data.network_step)
    print("second setup")
    assert len(paths_random) <= 6 and len(paths_random[0]) <= 20

def test_graph_multiprocessing_failures():
    """
    Just throwing this one in there, this is the
    last unit-testable function in graphing.py
    even though its just for fun/a joke. The 
    function is only used as a fun appendix
    and for our own explorartory purposes from
    the debugging stage of the project.

    It does prove that the functions runs
    to completion though so there's that.
    """
    assert graphing.graph_multiprocessing_failures() == "Joe Mama"
