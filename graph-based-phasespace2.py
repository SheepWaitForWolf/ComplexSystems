from pylab import *
import networkx as nx

g = nx.DiGraph()

for x in range(100):
    for y in range(100):
        g.add_edge((x, y), ((x ** x ) % 100, x))

ccs = [cc for cc in nx.connected_components(g.to_undirected())]
n = len(ccs)
w = ceil(sqrt(n))
h = ceil(n / w)
for i in xrange(n):
    subplot(h, w, i + 1)
    nx.draw(nx.subgraph(g, ccs[i]), with_labels = True)

show()

