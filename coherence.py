import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import numpy as np
from math import e

def initialize():
	global g, nextg, time, r
	time = 0
	thetas = []
	g = nx.karate_club_graph()
	g.pos = nx.spring_layout(g)
	for i in g.nodes_iter():
		g.node[i]['theta'] = 2 * pi * random()
		thetas.append(g.node[i]['theta'])
		g.node[i]['omega'] = 1. + uniform(-0.1, 0.1)
	nextg = g.copy()
	theta = np.sum(thetas)
	#r = abs(1/34 * e**(i * theta))
    
def observe():
    global g, nextg, time
    cla()
    nx.draw(g, cmap = cm.hsv, vmin = -1, vmax = 1,
            node_color = [sin(g.node[i]['theta']) for i in g.nodes_iter()],
            pos = g.pos)

alpha = 1 # coupling strength
Dt = 0.01 # Delta t

def update():
    global g, nextg, time
    for i in g.nodes_iter():
        theta_i = g.node[i]['theta']
        nextg.node[i]['theta'] = theta_i + (g.node[i]['omega'] + alpha * ( \
            sum(sin(g.node[j]['theta'] - theta_i) for j in g.neighbors(i)) \
            / g.degree(i))) * Dt
    g, nextg = nextg, g
    time = time + Dt

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])

subplot(1,1,1)
plot(time, r)
xlabel('t')
ylabel('r')
show()

