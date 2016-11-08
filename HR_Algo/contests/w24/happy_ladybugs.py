mport sys

Q = input()
for a0 in xrange(Q):
    alph = [0]*26
    empty = 0
    n = input()
    b = raw_input()
    prev = '_'
    trans = 0
    for i in b:
      if prev != i:
        prev = i
        trans += 1
      if not ord(i) == 95:
        alph[ord(i)-65] += 1
      else:
        empty += 1
    single = sum([1 for i in alph if i == 1])
    unique = len(set(b))
    if empty:
      unique -= 1 
    if single != 0:
      print 'NO'
      continue
    if unique == trans:
      print 'YES'
    elif empty != 0:
      print 'YES'
    else:
      print 'NO'
