from numpy import loadtxt,array,mean,linspace
from matplotlib.pyplot import axes,plot,show

data=loadtxt('src\ex1data1.txt',delimiter=",")
x=data[:,:-1]
y=data[:,-1]
m=y.shape[0]

l=list(data)

k=len(l)//10

def f(x):
    l.sort(key = lambda t:abs(t[0]-x))

    newdata=array(l)
    return mean(newdata[:k,-1])

# print(f(1))
pltx=linspace(0,25)

ax=axes()
ax.scatter(data[:,:-1],y)
plot(pltx,list(map(lambda x:f(x),pltx)))
show()