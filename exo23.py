from numpy import *
from pylab import *

#exo 3 TP2
#1a
def Z(n):
    U=rand(n)
    V=rand(n)
    return (U,V)
#1b
def f(n):
    [x,y]=Z(n);
    f=y*(sin(x*y))**2
    return f

#1c
def I(n):
    I=(1/n)*sum(f(n))
    return I
    












