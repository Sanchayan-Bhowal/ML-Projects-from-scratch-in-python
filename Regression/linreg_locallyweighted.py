from matplotlib.pyplot import axes,plot,show
from numpy import linalg,array,zeros,loadtxt,dot,std,concatenate,ones,linspace
from math import exp

def e(z):
    return array(list(map(lambda x:exp(-linalg.norm(x)**2/(2*tau**2)),z)))

def f(s):
    theta=zeros(x.shape[1]+1)
    z=array([1,s])
    w=array(list(map(lambda x:e(x-z),X)))[:,1]
    for _ in range(100):
        theta=theta+(alpha/m)*((y-dot(X,theta))*w).dot(X)
    return theta@z
tau=1
alpha=0.01
data=loadtxt('src\ex1data1.txt',delimiter=",")
x=data[:,:-1]
y=data[:,-1]
m=y.shape[0]

#feature normalization
sigma=std(x,axis=0)
x=x/sigma

X=concatenate([ones((m,1)),x],axis=1)

pltx=linspace(0,25)

ax=axes()
ax.scatter(data[:,:-1],y)
plot(pltx,list(map(lambda x:f(x/sigma),pltx)))
show()