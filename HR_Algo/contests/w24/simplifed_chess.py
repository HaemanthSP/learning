def kinght_moves(board, loc):
  moves = [[2,-1],[2,1],[1,-2],[1,2]]
  for mv in moves:
    x = loc[0] + mv[0]
    y = loc[1] + mv[1]
    if x in range(0,4) and y in range(0,4):
      board[x][y] += 1
  return board

def rook_moves(board, loc):
  moves1 = [[loc[0],i] for i in range(4) if not i == loc[1]]
  moves2 = [[loc[1],i] for i in range(4) if not i == loc[0]]
  moves = moves1 + moves2
  for mv in moves:
    x = mv[0]
    y = mv[1]
    if x in range(0,4) and y in range(0,4):
      board[x][y] += 1
  return board

def bishop_moves(board, loc):
  moves = [[-1,-1],[-1,1],[1,-1],[1,1]]
  for move in moves:
    diag = [[move[0]*i,move[1]*i] for i in range(1,4)]
    for mv in diag:
      x = loc[0] + mv[0]
      y = loc[1] + mv[1]
      if x in range(0,4) and y in range(0,4):
        board[x][y] += 1
  return board

def queen_moves(board, loc):
  board = rook_moves(board, loc)
  board = bishop_moves(board, loc)
  return board

def mult_lists(list1,list2):
  res = list1
  for i,l1,l2 in enumerate(zip(list1,list2)):
    for j,x,y in enumerate(zip(l1,l2)):
      res[i][j] = x*y
  return res
 
def add_val2list(l1,val)
  res = list1
  for i,l1 in enumerate(list1)):
    for j,x in enumerate(l1)):
      res[i][j] = x+val
  return res

def add_val_of_list(l1,val)
  res = 0
  for l1,l2 in zip(list1,list2):
    for x,y in zip(l1,l2):
      res += x+y
  return res


loc_map = {'A':0, 'B':1, 'C':2, 'D':3}
G = input()
for g in range(G):
  board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  #our_coins = {0:0, 1:0, 2,}
  result = ''
  w, b, m = map(int,raw_input().split())
  for i in range(w):
    t, c, r = raw_input().split()
    r = int(r)
    c = loc_map[c]
    loc = [c,r]
    if t == 'Q':
      board = queen_moves(board, loc)
    elif == 'R':
      board = rook_moves(board, loc)
    elif == 'B':
      board == bishop_moves(board, loc)
    elif == 'N':
      board == kinght_moves(board, loc)

  for i range(b):
    t, c, r = raw_input().split()
    r = int(r)
    c = loc_map[c]
    loc = [c,r]
    if t == 'Q':
      if board[c][r] != 0:
        result = 'YES'
      else:
        board1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        board1 = queen_moves(board1, loc)
        inf_bQ = add_val_of_list(mult_lists(board1,board))
        mv_bQ = np.sum(board1)
        diff = mv_bQ - inf_bQ
	overlap = np.sum(board-1)
	if diff == 0 and overlap > 0:
	  result = 'YES'
	else:
	  result = 'NO'

   print result
   # elif == 'R':
   #   board = rook_moves(board, loc)
   # elif == 'B':
   #   board == bishop_moves(board, loc)
   # elif == 'N':
   #   board == kinght_moves(board, loc)

