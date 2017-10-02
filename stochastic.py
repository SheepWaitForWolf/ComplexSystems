import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx

p = 0.3

def initialize():
	global g, nextg
	g = nx.karate_club_graph()
	g.pos = nx.spring_layout(g)
	for i in g.nodes_iter():
		g.node[i]['state'] = 1 if random() < .5 else 0
	nextg = g.copy()

def observe():
	global g, nextg
	cla()
	nx.draw(g, cmap = cm.binary, vmin = 0, vmax = 1,
	node_color = [g.node[i]['state'] for i in g.nodes_iter()],
	pos = g.pos)

def update():
	global g, nextg
	for i in g.nodes_iter():
		nextg.node[i]['state'] = 1 if random() > p \
					else 0 
	g, nextg = nextg, g

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
