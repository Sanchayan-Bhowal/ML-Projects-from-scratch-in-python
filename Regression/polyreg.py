from numpy import *
from matplotlib.pyplot import *

def cost(theta):
    return 0.5*sum((dot(X,theta)-y)**2)

def gradientdescent(theta):
    storecost=list()
    for j in range(1000):
        for i in range(m):
            theta=theta-(alpha/(m*(i+j+1)))*(dot(X[i],theta)-y[i])*X[i]
        storecost.append(cost(theta))
    return theta,storecost
alpha=0.01
k=3
data=loadtxt('src\ex1data1.txt',delimiter=",")
x=data[:,:-1]
y=data[:,-1]
m=y.shape[0]

mu=mean(x,axis=0)
sigma=std(x,axis=0)
x=(x-mu)/sigma

theta=zeros(k+1)
newdata=[x**i for i in range(k+1)]
X=concatenate(newdata,axis=1)

# print(X[:2,:])
theta,storecost=gradientdescent(theta)

# print()
pltx=linspace(-100,100)

ax=axes()
ax.scatter(data[:,:-1],y)
plot(pltx,polyval(theta,(pltx-mu)/sigma))
show()