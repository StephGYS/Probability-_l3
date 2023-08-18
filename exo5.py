from numpy import *
from pylab import *

#exo 4
def cauchy(n):
    x=rand(n)
    f=tan(pi*(x-1/2)) 
    M=cumsum(f)/arange(1,n+1)
    
    clf
    figure(1)
    subplot(3,1,1)
    plot(f)
    title('trajectoire de cauchy')
    subplot(3,1,2)
    plot(M)
    title('graphe des moyennes empiriques')
    subplot(3,1,3)
    hist(M)
    title('histogramme des moyennes empiriques')
    show()
    moy_final=M[n-1]
    return f
#test      
cauchy(50)