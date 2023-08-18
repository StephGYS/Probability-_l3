from numpy import *
from pylab import *

#exo 7

#2

def geometriq(N,p): 
    U=rand(N) 
    G= floor(log(1.0-U)/log(1-p)) + 1.0 
    return G

geometriq(17,0.5)

def binomneg(N,r,p): 

    X=rand(N,r)
    v=floor(log(1.0-X)/log(1-p))+1.0
    Y=sum(v,1)
    Z= cumsum(Y)/(arange(N)+1.0)
    
    clf()
    plot(Z)
    show()
    return Y,Z

#test
binomneg(10,5,0.3)