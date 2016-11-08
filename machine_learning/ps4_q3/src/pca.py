import numpy as np
import cv2
import matplotlib.pyplot as plt

def pca():
  img1 = cv2.imread("../images/1.jpg",0)
  img2 = cv2.imread("../images/2.jpg",0)
  img3 = cv2.imread("../images/3.jpg",0)
  img4 = cv2.imread("../images/4.jpg",0)
  img_1 = np.concatenate((img1,img2))
  img_2 = np.concatenate((img3,img4))
  img = np.concatenate((img_1,img_2))
  #img = img2
  cv2.namedWindow("image",0)
  cv2.imshow("image", img)
  p_h, p_w = 16, 16
  height, width = np.shape(img)
  h = height/p_h
  w = width/p_w
  X = np.zeros((w*h, p_h*p_w))

  for i in range(h):
    for j in range(w):
      x_vec = img[i*p_h:(i+1)*p_h,j*p_w:(j+1)*p_w].flatten()
      #mean = sum(x_vec)/(p_h*p_w)
      #var = ommitted since image pixels are in same scale
      X[(i*j)+j] = x_vec
      X -= sum(X)/(h*w*p_h*p_w)
  cov = np.dot(X.T,X)
  e_val, e_vec = np.linalg.eig(cov)
  
  res = np.dot(X,e_vec[40:42,:].T)
  plt.plot(res[0:1548,:][:,0], res[0:1548,:][:,1], linestyle=" ", marker="o", color = 'r') 
  plt.plot(res[1548:3096,:][:,0], res[1548:3096,:][:,1], linestyle=" ", marker="o", color = 'g') 
  plt.plot(res[3096:4644,:][:,0], res[3096:4644,:][:,1], linestyle=" ", marker="o", color = 'b') 
  plt.plot(res[4644:6192,:][:,0], res[4644:6192,:][:,1], linestyle=" ", marker="o", color = 'y') 
  return res

