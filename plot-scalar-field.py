from pylab import *

xvalues, yvalues = meshgrid(arange(-4, 4, 0.05), arange(-4, 4, 0.05))
zvalues = sin(xvalues * yvalues)

cp = contour(xvalues, yvalues, zvalues)
clabel(cp)

show()
