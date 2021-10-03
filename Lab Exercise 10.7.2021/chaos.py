from pylab import *
xvals = list(range(10))                     # make list of x values
yvals = [x**2 for x in xvals]     # make list of y values (list comprehension)
plot(xvals, yvals, 'r')       # plot x,y in red
show()                       # Output plot via TK
