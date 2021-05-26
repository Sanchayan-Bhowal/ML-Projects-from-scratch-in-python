from numpy import *
from matplotlib.pyplot import *

def cost(theta):
    return 0.5*sum((dot(X,theta)-y)**2)
def gradientdescent(theta):
    storecost=list()
    for _ in range(100):
        theta=theta-(alpha/m)*(dot(X,theta)-y).dot(X)
        storecost.append(cost(theta))
    return theta,storecost
alpha=0.01
data=loadtxt('ex1data2.txt',delimiter=",")
x=data[:,:-1]
y=data[:,-1]
m=y.shape[0]
theta=zeros(x.shape[1]+1)
#feature normalization
mu=mean(x,axis=0)
sigma=std(x,axis=0)
x=(x-mu)/sigma

#batch gradient descent
X=concatenate([ones((m,1)),x],axis=1)
theta,storecost=gradientdescent(theta)

pltx,plty=meshgrid(linspace(-2,3.2,10),linspace(-3,3,10))
z=theta[0]+theta[1]*pltx+theta[2]*plty
plt3d=figure()
ax=plt3d.add_subplot(111,projection='3d')
ax.plot_surface(pltx,plty,z,alpha=0.2)
ax.scatter3D(x[:,0],x[:,1],y)
# plot(arange(1,101),storecost)
show()