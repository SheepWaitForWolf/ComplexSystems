from pylab import *
import networkx as nx

g = nx.hypercube_graph(5)

nx.draw(g, with_labels = True)
show()
