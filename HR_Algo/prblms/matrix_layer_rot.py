import copy
import math
def mat2arr(mat, idx):
  print idx
  if not idx == 0:
    mat = mat[idx:-idx, idx:-idx]
  m, n = len(mat), len(mat[0])
  if m == 1 or n == 1:
    return mat.tolist()[0]
  
  slices = mat[::m-1]
  #columns = (mat.T)[::n-1]
  columns = [[x[0] for x in mat], [x[n-1] for x in mat]] 
  layer =  slices[0] + columns[1][1:-1] + slices[1][::-1]\
           + columns[0][1:-1][::-1]
  return layer 

def list2lyr(mat, idx):
 m = len(mat)
 n = len(mat[0])
 s = idx
 e = n - idx
 if idx == 0:
   e = None
 lyr = mat[idx][s:e]

def rot_arr(layer,r):
  n = len(layer)
  r = r%n
  if r == 0:
    return layer
  return layer[r:] + layer[:r]

def update_idx(e, step):
  s = e
  e = e + step
  return s, e

def arr2mat(mat, layer, i):
  print layer
  n, m = len(mat), len(mat[0])
  ml = m - 2*i
  nl = n - 2*i 
  e = ml
  
  if ml <= 1 or nl <=2:
    return mat
  ce = -i
  if i == 0:
    ce = None

  print layer[:e]
  mat[i::ml-2][0][i:ce] = layer[:e]
  print mat[i::ml-2][0][i:ce]
  s, e = update_idx(e,nl-2)
  print layer[s:e]
  for j in range(i+1,n-i-1):
    #mat[:,n-1-i][i+1:-(i+1)] = layer[s:e]
    #print mat[j][n-1-i],layer[s:e],j,i
    mat[j][m-1-i] = layer[s:e][j-i-1]
    print mat[j][m-1-i]
  s, e = update_idx(e,ml)
  print layer[s:e]
  mat[i::ml-1][1][i:ce] = layer[s:e][::-1]
  print mat[i::ml-1][1][i:ce]
  
  s, e = update_idx(e,nl-2)
  print layer[s:e]
  for j in range(i+1,n-i-1):
    #mat[:,i][i+1:-(i+1)] = layer[s:e][::-1]
    mat[j][i] = layer[s:e][::-1][j-i-1]
    print mat[j][i]
  return mat

def rot_mat_lyrs(mat, r):
  m, n = len(mat), len(mat[0])
  res_mat = copy.deepcopy(list(mat))
  iters = math.ceil((min(m,n) -1)/2.)
  for i in range(int(iters)):
    layer = mat2arr(res_mat, i)
    rot_layer = rot_arr(layer, r)
    res_mat = arr2mat(res_mat, rot_layer, i)
  return res_mat
