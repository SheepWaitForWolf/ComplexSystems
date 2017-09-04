from pylab import *

a = 1.1
K = 1
r = 2.5

def initialize():
	global x, result, t, timesteps
	x = 1
	result = [x]
	t = 0
	timesteps = [t]

def observe():
	global x, result, t, timesteps
	result.append(x)
	timesteps.append(t)

def f(x):
	return x + r * x * (1 - x / K)
	

def update():
	global x, result, t, timesteps
	x = f(x)
	t = t + 0.1

initialize()
while t < 10.:
	update()
	observe()


### drawing diagonal line
xmin, xmax = 0, 20
plot([xmin, xmax], [xmin, xmax], 'k')

### drawing curve
rng = arange(xmin, xmax, (xmax - xmin) / 100.)
plot(rng, map(f, rng), 'k')

### drawing trajectory
horizontal = [result[0]]
vertical = [result[0]] 
for x in result[1:]:
    horizontal.append(vertical[-1])
    vertical.append(x)
    horizontal.append(x)
    vertical.append(x)    
plot(horizontal, vertical, 'b')

show()
