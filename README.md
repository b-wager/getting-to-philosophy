# GettingToPhilosophy
The goal of our project is to analyze the most popular links on Wikipedia as well as
the most popular first links and where following them takes you.

We visualized the popularity using simple bar graphs from matplotlib, and used
PyGraphViz to create network graphs to visualize the paths. We based our project
around the wikipedia library, which is an API that allows us to access Wikipedia
pages easily from Python. Our full list of software packages can be found in
`requirements.txt`.

In order to get the `wikipedia` library to behave properly, you need to modify line 389 of
the wikipedia.py file in the wikipedia library to set `features="lxml"` so that it can parse
correctly without warnings. This change is taken as a parameter into the BeautifulSoup
command.

## Usage
Within our project is structured around the `create_link_list` function, which optionally
takes a depth and a threadcount (the defaults are threads=12 and depth=200), and returns
a list of lists where each interior list is the set of all links on a single Wikipedia
page. The usage of the term "threads" is not explicitly correct as while we treat them
as such, at the system level they are actually separate processes due to restricitons
imposed by Python's Global Interpreter Lock restricting Python processes to a single thread.
We then pass the link data from `create_link_list` to the `plot_frequency` function which
graphs the frequency of any data you give it via a bar plot. You can specify whether the
input is "flat" or not (whether it is a nested list or just a list) but the default is 
nested as that is what `create_link_list` will generate.

We also have the function `get_paths` which returns a list of page names. You can specify if
it should use `network_step` or `find_first_link`. `network_step` is meant to provide a
profile of how pages relate overall, as it follows random paths through links from page to page
while `find_first_link` gets the first link on a page. If the function has the proper return
type which is a list of pages, then it should in theory work properly. You will find many
functions in our project have an id parameter or similar, this is because they are meant to
be part of a multiprocessing pool and need to know where to put their output in the 
`return_dict`. `graph_network` takes the same data format as `plot_frequency`, except instead of
graphing their frequency it connects them as a network. While the actual datatype is the same,
`graph_network` acts as if they were ordered paths and for each internal list it treats it like
a sequence and plots them connected in that order. It saves the graphs as `file.png` in the
top-level directory of the project alongside the `main.ipynb` notebook.



