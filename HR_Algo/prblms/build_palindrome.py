def ptntl_substrng(str1, str2):

  m, n = len(str1), len(str2)
  ptntl_subs = []

  found = False
  for i in range(m):
    if found:
      break
    frwX = range(i+1)
    revX = frwX[::-1]
    for f,r in zip(frwX, revX):
      srch_str = str1[f:m-r]
      print srch_str
      l = len(srch_str)
      beg = 0
      while 1:
        last_loc = str2.find(srch_str[::-1], beg)
        if last_loc == -1:
          break
        # Use this to break in the first found level
        if l != m:
          found = True 
        #subset = [srch_str, f, last_loc, l]
        subset = [f, last_loc, l]
        print subset
        ptntl_subs.append(subset) 
        beg = last_loc + l
  
  return ptntl_subs
      
def generate_palindrome(str1, str2, ptntl_subs):

  res = []
  for subs in ptntl_subs:   
    loc1, loc2, l = subs
    print subs
    m, n = len(str1), len(str2)
    print m,n
    # First right
    if not loc1+l >= m:
      print "FR" 
      res.append(str1[loc1:loc1+l+1]+str1[loc1:loc1+l][::-1])
    # First left                                             
    if not loc1-1 < 0:                                       
      print "FL" 
      res.append(str1[loc1:loc1+l][::-1]+ str1[loc1-1:loc1+l])
    # Second right                                           
    if not loc2+l >= n:                                    
      print "SR" 
      res.append(str2[loc2:loc2+l+1]+str2[loc2:loc2+l][::-1])
    # Second left                                            
    if not loc2-1 < 0:                                       
      print "SL" 
      res.append(str2[loc2:loc2+l][::-1]+str2[loc2-1:loc2+l])
 
  return res

def buid_palindrome(str1, str2):

  m, n = len(str1), len(str2)
  s1 = str1 if m < n else str2
  s2 = str2 if s1 == str1 else str1
 
  ptntl_subs = ptntl_substrng(s1, s2)
  res = generate_palindrome(s1, s2, ptntl_subs)
  res.sort()
  print res
  if not res:
    return -1
  return res[0]
