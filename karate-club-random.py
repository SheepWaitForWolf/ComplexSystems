from pylab import *
import networkx as nx

g = nx.karate_club_graph()

subplot(2,2,1)
nx.draw(nx.gnm_random_graph(g.number_of_nodes(), g.number_of_edges()))
title('random karate')

#sequence = [1, 2, 3, 4]
#subplot(2,2,2)
#nx.draw(nx.random_degree_sequence_graph(sequence))
#title('random degree sequence')

z=[10 for i in range(100)]
subplot(2,2,3)
nx.draw(nx.expected_degree_graph(z))
title('expected degree graph')

#subplot(2,2,4)
#nx.draw(nx.double_edge_swap(g)
#title('double edge swap')


show()
