from numpy import *
from pylab import *

#exo 1 TP2


def ind1(x):
    Y=linspace(min(x)-1,max(x)+1,50)
    k=zeros(50);
    n=shape(x)[0]
    for i in range(n):
        k=k+ abs(Y-x[i])
    plot(Y,k,'r')
    return k
             

def ind2(x):
    Y=linspace(min(x)-1,max(x)+1,50)
    k=zeros(50);
    n=shape(x)[0]
    for i in range(n):
        k=k+ abs((Y-x[i])**2)
    plot(Y,k,'g')
    return k


def ind_inf(x):
    Y=linspace(min(x)-1,max(x)+1,50)
    k=zeros(50);
    n=shape(x)[0]
    for i in range(n):
        k=k+ max(abs(Y-x[i]))
    plot(Y,k,'b')
    return k
#test
x=[1,3,4]

ind1(x)
ind2(x)
ind_inf(x)