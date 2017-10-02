from pylab import *
import networkx as nx

g = nx.Graph()

g.add_nodes_from(['Daniel', 'Jim', 'Murray', 'Tony', 'Andrew', 'Scott', 'Danielle', 'Christina', 'Rachele', 'Ryan'])

g.add_edge('Daniel', 'Scott')
g.add_edge('Daniel', 'Christina')
g.add_edge('Daniel' , 'Jim')
g.add_edge('Daniel', 'Tony')
g.add_edge('Daniel' , 'Murray')
g.add_edge('Daniel', 'Andrew')
g.add_edge('Daniel' , 'Danielle')
g.add_edge('Daniel', 'Ryan')

g.add_edge('Tony' , 'Jim')
g.add_edge('Scott', 'Tony')

g.add_edge('Scott' , 'Danielle')
g.add_edge('Jim', 'Rachele')

g.node['Daniel']['job'] = 'Developer'
g.node['Daniel']['age'] = 28

g.node['Jim']['job'] = 'Art'
g.node['Jim']['age'] = 31

g.node['Tony']['job'] = 'Carer'
g.node['Tony']['age'] = 38

g.node['Christina']['job'] = 'Project Manager'
g.node['Christina']['age'] = 26

g.edge['Daniel']['Scott']['relationship'] = 'Friend'
g.edge['Daniel']['Jim']['relationship'] = 'Friend'
g.edge['Daniel']['Tony']['relationship'] = 'Friend'
g.edge['Daniel']['Andrew']['relationship'] = 'Friend'
g.edge['Daniel']['Murray']['relationship'] = 'Friend'
g.edge['Daniel']['Danielle']['relationship'] = 'Friend'

g.edge['Daniel']['Christina']['relationship'] = 'Girlfriend'
g.edge['Scott']['Danielle']['relationship'] = 'Girlfriend'
g.edge['Jim']['Rachele']['relationship'] = 'Girlfriend'

nx.draw(g, with_labels = True)
show()

