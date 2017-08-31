from pylab import *

a = 1.1
K = 5
r = 1
d = 0.9
b = 1
c = 1

def initialize():
	global x, y, xresult, yresult, t, timesteps
	x = 1
	y = 1
	xresult = [x]
	yresult = [y]
	t = 0
	timesteps = [t]

def observe():
	global x, y, xresult, yresult, t, timesteps
	xresult.append(x)
	yresult.append(y)
	timesteps.append(t)

def update():
	global x, y, xresult, yresult, t, timesteps
	nextx = x + r * x * (1 - x / K) - (1 - 1 / (b * y + 1)) * x
	nexty = y - d * y + c * x * y
	t = t + 0.1
	x, y = nextx, nexty

initialize()
while t < 10.:
	update()
	observe()

print xresult
print yresult
plot(timesteps, xresult)
plot(timesteps, yresult)
show()
