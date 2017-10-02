from pylab import *

a = 4
K = 50
r = a - 1

def initialize():
	global x, result, y, yresult, t, timesteps
	x = 1.001
	y = 1
	yresult = [y]
	result = [x]
	t = 0
	timesteps = [t]

def observe():
	global x, result, y, yresult, t, timesteps
	result.append(x)
	yresult.append(y)
	timesteps.append(t)

def update():
	global x, result, y, yresult, t, timesteps
	x = x + r * x * (1 - x / K)
	t = t + 0.1
	y = y + r * y * (1 - y / K)

initialize()
while t < 10.:
	update()
	observe()


# print result
plot(timesteps, result, 'b')
plot(timesteps, yresult, 'g--')
show()
