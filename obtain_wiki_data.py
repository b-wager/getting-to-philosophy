"""
Code used to obtain all links on random wikipedia pages using the wikipedia api.
"""

import multiprocessing
from random import choice
import wikipedia


def random_page(page=None):
    """
    Returns a random wikipedia page or a wikipedia page of choice.

    Args:
        page (optional): a string of the wikipedia page you want. If left
            blank, the page will be random.

    Returns: a random wikipedia page or the wikipedia page with the title page.
    """
    while page is None:
        title = wikipedia.random()
        try:
            page = wikipedia.page(title, auto_suggest=False)
        except wikipedia.DisambiguationError as error:
            options = error.options
            while True:
                temp = choice(options)
                try:
                    page = wikipedia.page(temp, auto_suggest=False)
                    break
                except wikipedia.DisambiguationError as error2:
                    options = error2.options
                    continue
                except wikipedia.PageError:
                    break
    return page


def network_step(depth, id_number, return_dict):
    """
    From a random wikipedia page, a random wikipedia link on that page is
    chosen. A wikipedia link that is embedded on that link's page is then
    chosen and so on and so forth for depth times. The "path" created by this
    process will be added to return_dict with a key of id_number.

    Args:
        depth: the integer number of links to follow.

        id_number: the identification integer for the current process (used to
            synchronize multiprocessing workers).

        return_dict: the dictionary in which the results of the process will
            be added.

    Returns:
        None.
    """
    pages = []
    page_titles = []
    pages.append(random_page())
    for i in range(1, depth):
        page = None
        while page is None:
            try:
                page = wikipedia.page(choice(pages[i - 1].links), auto_suggest=False)
            except wikipedia.PageError:
                continue
            except wikipedia.DisambiguationError as error:
                page = wikipedia.page(choice(error.options), auto_suggest=False)
        pages.append(page)
    for page in pages:
        page_titles.append(page.title)
    return_dict[id_number] = page_titles


def get_links(process_num, depth, return_dict):
    """
    A utility function used to assign all the links in a page with an id
    number depth times.

    Args:
        process_num: an integer representing the worker calling this function.

        depth: the integer number of times the worker will be adding a random
        page's links to return_dict.

        return_dict: the dictionary to which the results of the processes will
        be added.

    Returns:
        None.
    """
    for i in range(depth):
        return_dict[process_num * depth + i] = random_page().links


def create_link_list(threads=12, depth=200):
    """
    Creates a multiprocessing process to obtain the list of links from threads
    * depth random wikipedia pages.

    Args:
        threads (optional): the integer number of workers to be active.
        Default is 12.

        depth (optional): the integer number of link lists each worker
        generates. Default is 200.

    Returns:
        A list of lists where each interior list is a list of the links from
        a random wikipedia page.
    """
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(threads):
        process = multiprocessing.Process(
            target=get_links, args=(i, depth, return_dict)
        )
        jobs.append(process)
        process.start()

    for proc in jobs:
        proc.join()
    all_links = return_dict.values()
    print("Done")
    return all_links
