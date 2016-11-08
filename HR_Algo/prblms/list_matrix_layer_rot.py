import copy
import math

def mat2lyr(mat, idx):
  m, n = len(mat), len(mat[0])
  ms, me, ns, ne = 0+idx, m-idx-1, 0+idx, n-idx-1
  layer = [[]]  

  layer = mat[ms][ns:ne+1] # Top
  layer = layer + [mat[i][ne] for i in range(ms+1,me)] # Right
  # To prevent redundency 
  if me-ms <=0 or ne-ns <=0:
    return layer 
  layer = layer + mat[me][ns:ne+1][::-1] # Bottom
  layer = layer + [mat[i][ns] for i in range(ms+1,me)][::-1] # Left
  
  return layer

def rot_arr(layer,r):
  n = len(layer)
  r = r%n
  if r == 0:
    return layer
  return layer[r:] + layer[:r]

def lyr2mat(mat, layer, idx):
  m, n = len(mat), len(mat[0])
  ms, me, ns, ne = 0+idx, m-idx-1, 0+idx, n-idx-1
  
  # Top
  s, e = 0, ne+1-ns
  mat[ms][ns:ne+1] = layer[s:e]

  # Right
  if me-(ms+1) > 0:
    s = e
    e = s + me-(ms+1)
    for i,j in enumerate(range(ms+1,me)):
      mat[j][ne] = layer[s+i]

  # Bottom
  s = e
  e = s + (ne+1)-ns 
  mat[me][ns:ne+1] = layer[s:e][::-1]
 
  # Left 
  id_arr = range(ms+1,me)[::-1]
  for i,j in enumerate(id_arr):
    mat[j][ns] = layer[e+i]
   
  return mat

def rot_mat_lyrs():
  m, n, r = map(int,raw_input().split())
  res_mat = [[]]*m
  for i in range(m):
    res_mat[i] = map(int,raw_input().split())
  iters = math.ceil((min(m,n) -1)/2.)
  for i in range(int(iters)):
    layer = mat2lyr(res_mat, i)
    rot_layer = rot_arr(layer, r)
    res_mat = lyr2mat(res_mat, rot_layer, i)
  return res_mat
