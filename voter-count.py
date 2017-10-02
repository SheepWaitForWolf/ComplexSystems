import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import random as rd

def initialize():
	global g, count
	count = 0
	g = nx.karate_club_graph()
	g.pos = nx.spring_layout(g)
	for i in g.nodes_iter():
		g.node[i]['state'] = 1 if random() < .5 else 0

def observe():
	global g, count
	print count
	cla()
	nx.draw(g, cmap = cm.binary, vmin = 0, vmax = 1,
		node_color = [g.node[i]['state'] for i in g.nodes_iter()],
		pos = g.pos)

def update():
	global g
	listener = rd.choice(g.nodes())
	speaker = rd.choice(g.neighbors(listener))
	g.node[listener]['state'] = g.node[speaker]['state']
	count += 1

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
