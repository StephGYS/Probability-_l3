from numpy import *
from pylab import *


#exercice 1
help(rand)
help(plot)
help(subplot)
help(hist)
help(cumsum) #somme cumulaire
help(shape)
Y=rand(10)  #2
Y=8*rand(10)-5  #3
#Y2=random(-3,5,100)
#4
Y=rand(100) 
#5
figure(0)
x1=rand(100)
N=arange(1,101)
Z1=cumsum(x1)*(1/N)
print(Z1)
plot(Z1)

#6
clf()
figure(1)
x2=3*rand(100)+3
N=arange(1,101)
Z2=cumsum(x2)*(1/N)
print(Z2)
plot(Z2)

#7
moy_emp=cumsum(x2)/N  #la moyenne empirique tend bien vers la moyenne 

#8 voir graphe

#Exercice2 
#1
def bernouilli(n,p):
    x=rand(n);
    Y=x<p; #1a
    clf()
    figure(2)
    subplot(211)
    plot(arange(1,n+1),Y) #1b
    title('trajectoire de X')
    Z=cumsum(Y)/ arange(1,n+1) #1c
    subplot(212)
    hist(Z)
    title('histogramme de de la moyenne empirique')
    show()
    return Y
#test
bernouilli(100, 0.8)
   
#2
def Expon(N,lamb):
    x=rand(N)
    f=-log(ones(N)-x)/lamb #Inverse de la fonction de repartition de la loi exponentielle f(x)=a.exp(-a.x)
    M=cumsum(f)/arange(1,N+1)
    clf()
    figure(3)
    subplot(3,1,1)
    plot(f)
    title('trajectoire de la loi')
    subplot(3,1,2)
    plot(M)
    title('graphe des moyennes empiriques')
    subplot(3,1,3)
    hist(M)
    title('histogramme des moyennes empiriques')
    show()
    return f
#test      
Expon(10,1)  



    
        


