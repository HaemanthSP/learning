import numpy as np
import matplotlib.pyplot as plt

def load_data():
 
  f = open('./data/x.txt' , 'r')
  x = np.array([map(float,line.split(',')) for line in f ])
  f.close()
  f = open('./data/y.txt', 'r')
  y = np.array([map(float, line.split()) for line in f])
  y = y.T[0]
  f.close
  return x, y



def predict(x, tau):
  #X_train, Y_train = load_data()
  X_train = np.loadtxt("./data/x.txt")
  Y_train = np.loadtxt("./data/y.txt")

  x1_p = X_train[np.argwhere(Y_train==1)]
  x2_p = X_train[np.argwhere(Y_train==0)]
  plt.plot(x1_p[:,:,0], x1_p[:,:,1], linestyle=' ', marker='o', color='b')
  plt.plot(x2_p[:,:,0], x2_p[:,:,1], linestyle=' ', marker='*', color='r')  
  #plt.scatter(X_train[:,1], X_train[:,0],c=np.array([Y_train]).T)
  y = lwlr(X_train, Y_train, x, tau)

def lwlr(X_train, Y_train, x, tau):
  theta = np.array([0.1, 0.2])
  theta_old = theta
  identity = np.eye(2)
  while 1:
    theta_old = theta
    d0 = np.subtract.outer(x[0], X_train[:,0])
    d1 = np.subtract.outer(x[1], X_train[:,1])
    dist = np.hypot(d0, d1)
    w = np.exp(-(abs(dist)**2)/2*tau**2)
    net = np.dot(X_train, theta.T) 
    hypo = 1/(1+np.exp(-net))
    z = w * ( Y_train - hypo)
    grad = np.dot(X_train.T, z) - 0.0001 * theta 
    D = np.diag(- w * hypo * (1-hypo))
    H = np.dot(X_train.T, np.dot(D, X_train)) - 0.0001 * identity
    theta = theta - np.dot(np.linalg.inv(H), grad) 
    print theta 
    if theta[0] == theta_old[0]:
      print "converged"
      break
  x1 = theta[1]/theta[0]
  x2 = - theta[1]/theta[0]
  plt.plot((x1,x2),(-1,1),'k-')
  print x1,x2,x
  plt.plot(x[0], x[1], marker='o', color='g')
