import matplotlib
matplotlib.use('TkAgg')
from pylab import *

n = 100 # size of space: n x n
p = 0.1 # probability of initially panicky individuals

def initialize():
    global config, nextconfig, density, timesteps, t
    config = zeros([n, n])
    density = []
    for x in xrange(n):
        for y in xrange(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
    t = 0
    timesteps = [t]
    
def observe():
    global config, nextconfig, density, timesteps, t
    density.append(config.tolist().count(1))
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)
    timesteps.append(t)

def update():
    global config, nextconfig, timesteps, t
    for x in xrange(n):
        for y in xrange(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
            nextconfig[x, y] = 1 if count in [2, 3] else 0
    config, nextconfig = nextconfig, config

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
import pylab

plot(density)
show()
