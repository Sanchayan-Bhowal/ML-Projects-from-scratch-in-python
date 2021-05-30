from numpy import *
from matplotlib.pyplot import *

def h_sub(o):
    return array(list(map(lambda x:1/(1+math.exp(-x)),o)))
def log(o):
    return array(list(map(math.log,o)))
def h(o):
    t=dot(X,o)
    return array(list(map(lambda x:1/(1+math.exp(-x)),t)))

def cost(theta):
    return sum(y.dot(log(h(theta))) + (1-y).dot(log(1-h(theta))))

def newton_rhapson(theta):
    storecost=list()
    D=zeros((m,m))
    fill_diagonal(D,(h(theta)).dot(h(theta)-1))
    H= X.T @ D @ X
    for _ in range(100):
        theta=theta-linalg.inv(H) @ ((h(theta)-y).dot(X))
        storecost.append(cost(theta))
    return theta,storecost

x=loadtxt(r'src\x.txt',delimiter=",")
y=loadtxt(r'src\y.txt',delimiter=",")
m=y.shape[0]
theta=zeros(x.shape[1]+1)

#batch gradient descent
X=concatenate([ones((m,1)),x],axis=1)
theta,storecost=newton_rhapson(theta)

pltx,plty=meshgrid(linspace(-2,3.2,10),linspace(-3,3,10))
temp=theta[0]+theta[1]*pltx+theta[2]*plty
z=apply_along_axis(lambda x:h_sub(x),axis=0,arr=temp)

plt3d=figure()
ax=plt3d.add_subplot(111,projection='3d')
ax.plot_surface(pltx,plty,z,alpha=0.2)
ax.scatter3D(x[:,0],x[:,1],y)
# plot(arange(1,101),storecost)
show()