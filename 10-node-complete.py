from pylab import *
import networkx as nx

g = nx.complete_graph(10)


g.add_node(10)

g.add_edges_from([(0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10)])

subplot(2,2,1)
nx.draw_circular(g, with_labels = True)

subplot(2,2,2)
nx.draw_random(g, with_labels = True)

subplot(2,2,3)
nx.draw(g, with_labels = True)

subplot(2,2,4)
nx.draw_spectral(g, with_labels = True)

show()
