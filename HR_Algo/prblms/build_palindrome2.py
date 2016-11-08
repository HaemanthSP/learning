def filter_ptntl_cntrs(inp_str):
  num_arr = [ord(c)-96 for c in inp_str]
  cnt_arr = []
  for i in range(len(num_arr)-2):
    if num_arr[i] == num_arr[i+2]:
      cnt_arr.append(i+1)
  return cnt_arr

def find_max_length(inp_str, cnt_arr):
  l = len(inp_str) - 1
  palind_arr = []
  for c in cnt_arr:
    mx = min(c - 0, l - c)
    mxl = 1 
    for i in range(2, mx+1):
      
      if inp_str[c-i] != inp_str[c+i]:
        break
      else:
	mxl += 1
    left = c - mxl
    right = l - (c+mxl)
    subset = [c, mxl, left, right, mxl + max(left, right)]
    palind_arr.append(subset)
    palind_arr.sort(key=lambda x: x[4]) 
  return palind_arr[::-1]


def ptntl_substrng(str1, str2, data_arr):
 
  palind_arr = []
  for subset in data_arr:
    c, mxl, l, r, mx_poss_len = subset
    srch_str1 = str1[:l]
    srch_str2 = str1[-r:]
    print srch_str1, srch_str2
    for j,srch_str in enumerate([srch_str1, srch_str2]): 
      for i in range(len(srch_str)):
        if j == 0:
          srch_sub =  srch_str[i:]
        else:
	  print i
          srch_sub =  srch_str[:-i]
	  print srch_sub
        if str2.find(srch_sub[::-1]) != -1:
          if j == 0:
            palindrome = srch_sub + str1[c-mxl:c+mxl+1] + srch_sub[::-1]
          else:
            palindrome = srch_sub[::-1] + str1[c-mxl:c+mxl+1] + srch_sub
          max_len_found = (len(palindrome)/2) - 1
          palind_arr.append(palindrome) 
          break
  
  return palind_arr

def identify_true_neigh():
  
  return

def evaluate_curr_best():
  return
