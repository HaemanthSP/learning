import numpy as np
import matplotlib.pyplot as plt
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x,y)

def generator(M):
  cart_coord = np.zeros((M,2))
  polar_coord = np.zeros((M,2))
  for x in range(M):
    y = np.sqrt(np.square(1-x)) ;
    
    cart_coord[x][0] = x
    cart_coord[x][1] = y

    i, j = pol2cart(x, y)
    
    polar_coord[x][0] = i
    polar_coord[x][1] = j

    plt.plot(cart_coord[:,0], cart_coord[:,1], linestyle=" ", marker='o', color="r")
    #plt.plot(polar_coord[:,0], polar_coord[:,1], linestyle=" ", marker='o',color = 'b')
    
