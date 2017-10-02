from pylab import *

r = 0.2
K = 1.0
Dt = 0.01
a = 1
b = 1
c = 1
d = 1

def initialize():
    global x, y, xresult, yresult, t, timesteps
    x = 0.1
    y = 0.1
    xresult = [x]
    yresult = [y]
    t = 0.
    timesteps = [t]
    
def observe():
    global x, y, xresult, yresult, t, timesteps
    xresult.append(x)
    yresult.append(y)    
    timesteps.append(t)

def update():
    global x, y, xresult, yresult, t, timesteps
    nextx = a * x - b * x * y
    nexty = -c * y + d * x * y
    x, y = nextx, nexty
    t = t + Dt

initialize()
while t < 50.:
    update()
    observe()

plot(xresult, yresult)
show()

