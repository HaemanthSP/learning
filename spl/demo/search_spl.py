import numpy as np
import scipy.signal as si
import time
import random

debug = False
ref_board = None
moves = 0
board = np.zeros((10,10))
explored_board = np.zeros((10,10)) - 1

def last_move_status():
  return

def search_letter(board, kernal):
  lrt_wt = si.correlate2d(board, kernal, mode='valid')/np.sum(kernal)
  #print lrt_wt
  mx = np.amax(lrt_wt)
  mx_id = np.argwhere(lrt_wt == mx)
  return mx, mx_id

def decide_char():
  
  return

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
  x = -1
  y = -1
  while(True):
    print 'random search'
    x = random.randint(4,5)
    y = random.randint(0,9)
    if (explored_board[x,y] != -1) or (x == -1):
      continue
    if validator(x,y):
      break 
  return x,y

def game(ref_brd):
  global ref_board
  global board
  global explored_board
  global moves
  
  ref_board = None
  moves = 0
  board = np.zeros((10,10))
  explored_board = np.zeros((10,10)) - 1

  ref_board = ref_brd 
  x,y = explorer()
  board[x,y] = explored_board[x,y] = 1
  # Filters for each characters
  s_krnl = np.array([[1,1],[1,0],[1,1],[0,1],[1,1]]) 
  p_krnl = np.array([[1,1,1],[1,0,1],[1,2,1],[1,0,0],[1,0,0]])
  l_krnl = np.array([[1,0],[1,0],[1,0],[1,0],[1,1]]) 

  spl_krnl = [s_krnl, p_krnl, l_krnl]
  #spl_krnl = [l_krnl]
  chr_found = [False, False, False] 
  while(True):
    selected_poses = []
    for i, krnl in enumerate(spl_krnl):
      if chr_found[i] == False:
        sim = search_letter(board, krnl)
      print 'sim', sim[0]
      if sim[0] != 1:
        subset = [sim[0], sim[1], krnl]
        selected_poses.append(subset)
        if debug:
          print sim
      else:
        print 'one char'
        x,y = explorer()
        continue
              
    selected_poses = sorted(selected_poses,key=lambda l:l[0], reverse=True)
    #print selected_pos
    print "running"
    found = False
    for selected_pose in selected_poses: 
      mx, poses, krnl = selected_pose
      #print mx
      if found:
        break
      for pos in poses:
        x, y = decide_nxt_mov(pos, board, krnl)
       
        if (explored_board[x,y] != -1) or (x == -1):
          continue
        
        if validator(x,y): 
		found = True
		break
        else:
          print 'wrong move'
          explored_board[x,y] = 0
      print explored_board * -1
    #print ref_board - 1 
    time.sleep(2) 
  return

def validator(x,y):
  global ref_board
  global board
  global explored_board
  global moves

  print 'curr mov:' , x,y
  moves = moves + 1
  print 'moves:', moves

  if ref_board[x,y] == 1:
    explored_board[x,y] = 1
    board[x,y] = 1
    return True
  else:
    explored_board[x,y] = 0  
  return False 
