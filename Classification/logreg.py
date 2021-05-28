from numpy import *
from matplotlib.pyplot import *

def h_sub(o):
    return array(list(map(lambda x:1/(1+math.exp(-x)),o)))
def h(o):
    t=dot(X,o)
    return array(list(map(lambda x:1/(1+math.exp(-x)),t)))

def cost(theta):
    return 0.5*sum((h(theta)-y)**2)

def gradientdescent(theta):
    storecost=list()
    for _ in range(1000):
        theta=theta-(alpha/m)*(h(theta)-y).dot(X)
        storecost.append(cost(theta))
    return theta,storecost
alpha=0.01
x=loadtxt(r'src\x.txt',delimiter=",")
y=loadtxt(r'src\y.txt',delimiter=",")
m=y.shape[0]
theta=zeros(x.shape[1]+1)

#batch gradient descent
X=concatenate([ones((m,1)),x],axis=1)
theta,storecost=gradientdescent(theta)

pltx,plty=meshgrid(linspace(-2,3.2,10),linspace(-3,3,10))
temp=theta[0]+theta[1]*pltx+theta[2]*plty
z=apply_along_axis(lambda x:h_sub(x),axis=0,arr=temp)

plt3d=figure()
ax=plt3d.add_subplot(111,projection='3d')
ax.plot_surface(pltx,plty,z,alpha=0.2)
ax.scatter3D(x[:,0],x[:,1],y)
# plot(arange(1,1001),storecost)
show()