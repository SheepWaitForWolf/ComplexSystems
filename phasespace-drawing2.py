from pylab import *

def initialize(x0, y0): ###
	global x, y, xresult, yresult
	x = x0
	y = y0
	xresult = [x]
	yresult = [y]

def observe():
	global x, y, xresult, yresult
	xresult.append(x)
	yresult.append(y)

def update():
	global x, y, xresult, yresult
	nextx = x + 0.1 * (x - x * y)
	nexty = y + 0.1 * (y - x * y)
	x, y = nextx, nexty

for x0 in arange(-2, 2, 0.5): ###
	for y0 in arange(-2, 2, 0.5): ###
		initialize(x0, y0) ###
		for t in xrange(30):
			update()
			observe()
		plot(xresult, yresult, 'b') ###

show()
