from numpy import *
from matplotlib.pyplot import *

x=loadtxt(r'src\x.txt',delimiter=",")
y=loadtxt(r'src\y.txt',delimiter=",")
m=y.shape[0]

data=column_stack((x,y))

l=list(data)

k=10

def f(x):
    l.sort(key = lambda t:(t[0]-x)**2+(t[1]-x)**2)

    newdata=array(l)
    return mean(newdata[:k,-1])*2-1

pltx=linspace(-1,1)
data_1=array(list(filter(lambda x:x[2]==1,data)))
data_2=array(list(filter(lambda x:x[2]==0,data)))
ax=axes()
ax.scatter(data_1[:,0],data_1[:,1])
ax.scatter(data_2[:,0],data_2[:,1],c='r')
plot(pltx,list(map(lambda x:f(x),pltx)))
show()