from numpy import*
from matplotlib.pyplot import*

def cost(theta):
    return 0.5*sum((dot(X,theta)-y)**2)
alpha=0.01
data=loadtxt('src\ex1data2.txt',delimiter=",")
x=data[:,:-1]
y=data[:,-1]
m=y.shape[0]
theta=zeros(x.shape[1]+1)
#feature normalization
mu=mean(x,axis=0)
sigma=std(x,axis=0)
x=(x-mu)/sigma

#minbatch gradient descent
X=concatenate([ones((m,1)),x],axis=1)
storecost=list()
for j in range(100):
    for i in range(m//3):
        theta=theta-(alpha/m)*(dot(X[3*i:3*i+3],theta)-y[3*i:3*i+3]).dot(X[3*i:3*i+3])
    storecost.append(cost(theta))

plot(arange(1,101),storecost)

show()