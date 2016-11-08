import numpy as np
import matplotlib.pyplot as plt
import os

def cluster_data(k):

 X = np.loadtxt("../data/X.txt")

 #plt.plot(X[:,0],X[:,1], linestyle = " ", marker = 0)
 clust_cent = np.random.random((k, 2))
 cluster = np.zeros(np.shape(X)[0])
 chroma = ["b", "r", "g","y","c","M"] 
 while 1: 
  for i,x in enumerate(X):
    dist = [np.hypot(x[0] - x0[0], x[1]-x0[1]) for x0 in clust_cent]
    cluster[i] = dist.index(min(dist))

  for i in range(k): 
    xi = X[np.argwhere(cluster == i)][::,0]
    if len(xi) == 0:
     continue
    clust_cent[i] = sum(xi)/len(xi)
    plt.plot(xi[:,0],xi[:,1], linestyle=' ', marker= 'o', color=chroma[i]
)
    plt.plot(clust_cent[i][0], clust_cent[i][1], marker='*', color=chroma[i])
  if raw_input() == 'q':
    plt.close()
    break 
  plt.close()
