import numpy as np
from matplotlib import pyplot as plt

#构造带噪声的y=x数据点
X = np.arange(-10,10,0.1)  #x数据区间[-10,10]，间隔0.1
m = X.shape[0]
err = np.random.normal(0,0.05,size = X.shape)  #噪声沿均值为0，标准差0.05的正态分布
Y = X + err

#前处理
X_data = np.zeros([X.shape[0],2])
X_data[:,1] = X   #为自变量增加常数列
Theta0 = np.random.uniform()*15
Theta1 = np.random.uniform()
Theta = np.array([[Theta0],[Theta1]])  #随机初始化参数θ1和θ2
alpha = 0.001
lam = 0.1    #设置学习步长和正则化参数
iteration = 1500    #设置迭代次数
plt.plot(X,np.dot(X_data,Theta),color = 'black',label = 'without regression')
print('Theta matrix after random initialization')
print(Theta)
print('y = θ0 + θ1*x')
#开始线性回归
for count in range(iteration):

    #计算代价函数(cost function)
    y_out = np.dot(X_data,Theta)  #计算取定θ下的输出y值
    
    dif = y_out[:,0]-Y
    regular_J=(sum([i*i for i in Theta])-Theta[0]*Theta[0])*lam
    J = (dif*dif).sum(0)/(2*m) +regular_J

    #进行梯度下降
    regular_T=Theta
    regular_T[0]=0.0
    tmp = np.zeros(Theta.shape)
    tmp[:,0] =((X_data.T.dot(dif))*alpha/m)[:] 
    Theta=Theta- tmp +lam*regular_T/m

plt.scatter(X,Y,label = 'data points')
plt.plot(X,np.dot(X_data,Theta),color = 'r',label = 'after regression')
plt.legend(loc = 'upper left')
plt.show()
print('\n')
print('Theta matrix after regression')
print(Theta)