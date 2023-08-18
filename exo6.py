from numpy import *
from pylab import *

#exo 6

#help(floor) #renvoir la partie entier inferieur
#help(round)
#help(ceil)   #renvoir la partie entier superieur
#help(mod)   #reste de la division euclidienne
#help(divmod) #le resultat et le reste de la division euclidienne

#2
ceil(10*rand(10))

#3
def binomiale(n,p,N):
    X=rand(N,n) #echantillon
    b=1.0*(X<p)  #loi binouilli
    B=sum(b,1)  #loi binomiale, sum(v,1) somme en ligne 
    somm=cumsum(B)/(1+arange(N))
   
    clf() 
    subplot(2,1,1)
    title('trajectoire de binomiale')
    plot(B)
    subplot(2,1,2)
    title('LGN')
    plot(somm)
    show()
    return(B,somm)
    
#test
binomiale(4,0.5,10)
    
 
