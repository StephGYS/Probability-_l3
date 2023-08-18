from numpy import *
from pylab import *

#exo 7

#2

def geometriq(N,p): 
    U=rand(N) 
    G= floor(log(ones(N)-U)/log(1-p)) + ones(N) 
    return G

