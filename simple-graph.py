import networkx as nx

#create new graph object
g = nx.Graph()

g.add_nodes_from(['1', '2', '3', '4', '5', '6'])

g.add_edges_from([('1', '2'), ('1', '4'), ('1','5'), ('2', '3'), ('2', '4'), ('3', '4'), ('3','5'), ('3', '6'), ('4', '6')])

g.nodes()
g.edges()
