def populator(inp_str):
  frq_arr = [0]*26
  for ele in inp_str:
    i = ord(ele) - 97
    frq_arr[i]+=1
  return frq_arr

def validator(inp_str):
  frq_arr = populator(inp_str)
  dense_arr = [x for x in frq_arr if x != 0]
  print dense_arr
  min_val, max_val = min(dense_arr), max(dense_arr)
  print [x - min_val for x in dense_arr], [max_val - x for x in dense_arr]
  way1 = [x - min_val for x in dense_arr]
  way2 = [max_val - x for x in dense_arr]
  w1 = sum([1 for x in way1 if x==0])
  w2 = sum([1 for x in way2 if x==0])
  print w1, w2 
  n = len(dense_arr)
  print w1+w2 , n
  if (w1+w2) == 2*n:
    return True
  is_valid = (w1+w2) == n 
  print (min(sum(way1),sum(way2))==1) , (min_val == 1 and w1==1)
  print min_val, max_val, w1, w2, n
  if is_valid:
    print w1
    is_valid = (min(sum(way1),sum(way2))==1) or (min_val == 1 and w1==1)
  return is_valid
