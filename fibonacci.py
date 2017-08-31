from pylab import *

def initialize():
	global x, a, y, result
	x = 1
	a = 0
	y = 1
	result = [x, y]

def observe():
	global x, result
	result.append(x)

def update():
	global x, y, result
	y = result[-2]
	x = result[-1]
	x = x + y

initialize()
for t in xrange(30):
	update()
	observe()

print result
