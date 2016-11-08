import numpy as np
import scipy.signal as si
import time
import random

debug = False
ref_board = None
moves = 0
board = np.zeros((10,10))
explored_board = np.zeros((10,10)) - 1
state = 0
rand_moves = []
pred_moves = []
success = False

s_krnl = np.array([[1,1],[1,0],[1,1],[0,1],[1,1]]) 
p_krnl = np.array([[1,1,1],[1,0,1],[1,1,1],[1,0,0],[1,0,0]])
l_krnl = np.array([[1,0],[1,0],[1,0],[1,0],[1,1]]) 
spl_krnl = [s_krnl, p_krnl, l_krnl]
chr_found = [False, False, False]

def search_letter(board, kernal):
  lrt_wt = si.correlate2d(board, kernal, mode='valid')/np.sum(kernal)
  #print lrt_wt
  mx = np.amax(lrt_wt)
  mx_id = np.argwhere(lrt_wt == mx)
  return mx, mx_id

def decide_nxt_mov( brd_loc, board, kernal):
  x, y = brd_loc
  xl, yl = np.shape(kernal)
  
  if debug:
   print x,y,xl,yl
  dense_kernal = np.ones((3,3))
  char_reg = board[x:x+xl,y:y+yl]
  #print np.size(char_reg) 
  if np.size(char_reg) != np.size(kernal):
    return [-1,-1] 
  # Finding the best of missing pixels
  f1 = kernal + char_reg
  f2 = kernal - char_reg
  f3 = si.convolve2d(f1, dense_kernal, mode=1)
  f4 = f3 * f2

  # Offset correction
  loc = np.argwhere(f4==np.amax(f4))
  brd_loc = brd_loc + loc

  return brd_loc[0]

def explorer():
  mov_list = []
  y_array = random.sample(range(0, 10), 10)
  x_array = range(4, 6)
  for x in x_array:
    mov_list.extend(zip([x] * 10, y_array))
  random.shuffle(mov_list)
  #for i in range(20):
  #  print 'random search'
  #  x = random.randint(4,5)
  #  y = random.randint(0,9)
  #  if (explored_board[x,y] != -1) or (x == -1):
  #    continue
  #  mov_list.append([x,y])

  return mov_list

def coord_to_idx(coord):
  idx = coord[0] * 10 + coord[1] + 1
  return idx

def idx_to_coord(idx):
  x = idx/10
  y = idx%10 - 1
  return [x,y]

def what_next(idx, res_board):
 
  global explored_board
  global board
  global state, success, rand_moves, pred_moves
   
  explored_board = res_board

  # Print for debug
  print 'Success:', success
  print 'State:', state
  print 'Recieved Idx', idx
  
  if idx != None:
    print '#1'
    x,y = idx_to_coord(idx)
    board[x,y] = explored_board[x,y]
    success = board[x, y] == 1
  else:
    print '#2'
    success = False
   
  if state == 0:
    if success:
      print '#3'
      state = 1 
    if not rand_moves or state != 1:
      print '#4'
      rand_moves = explorer()
      print 'Rand moves', rand_moves
    return coord_to_idx(rand_moves.pop())
    
  if state == 1:
    print '#5'
    if success or not pred_moves:
      print '#6'
      pred_moves = predict()
      print 'Pred moves', pred_moves
    return coord_to_idx(pred_moves.pop())
 
def predict():
  global pred_moves, state, rand_moves, chr_found
  
  selected_poses = []
  for i, krnl in enumerate(spl_krnl):
    if chr_found[i] == False:
      sim = search_letter(board, krnl)
    else:
      continue
    print 'sim', sim[0]
    if sim[0] != 1:
      subset = [sim[0], sim[1], krnl]
      selected_poses.append(subset)
    else:
      print '#7'
      state = 0
      remove_char( sim[1], krnl)
      chr_found[i] = True
      return [rand_moves.pop()]
            
  selected_poses = sorted(selected_poses,key=lambda l:l[0], reverse=True)
  found = False
  for selected_pose in selected_poses: 
    mx, poses, krnl = selected_pose
    if found:
      break
    for pos in poses:
      x, y = decide_nxt_mov(pos, board, krnl)
      if (explored_board[x,y] != -1) or (x == -1):
        continue
      pred_moves.append([x,y])
  return pred_moves

def remove_char(loc, kernal):
  global board
  x, y = loc
  xl, yl = np.shape(kernal)
  board[x:x+xl,y:y+yl] -= kernal
  return
