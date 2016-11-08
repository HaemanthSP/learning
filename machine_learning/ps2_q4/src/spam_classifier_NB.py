import numpy as np

phy_y1 = {} 
phy_y0 = {}
py1 = 1;
py0 = 1;

def parse_data(line):
 data = {}
 data = {int(x.split(" ")[0]): int(x.split(" ")[1]) for x in line.split(", ")}
 return data

def train():
 
 def test_func():
  print "Test.....!"
 
 test_func()
 phy_y1 = {}
 phy_y0 = {}
 phy_y1.update(dict.fromkeys(range(1448),0))
 phy_y0.update(dict.fromkeys(range(1448),0))
 y0 = 0
 y1 = 0
 spam_tot_w = 0
 nspam_tot_w = 0

 # Loading and training data
 f = open("../spam_train_trial.txt")
 print  "Training......"
 for line in f:
   train_data = parse_data(line)
   if train_data[1447] == 1:
     for k in train_data.iterkeys():
       if k == 1447:
         continue
       phy_y1[k] += train_data[k]
       spam_tot_w += train_data[k]
     y1 = y1+1
   else:
     for k in train_data.iterkeys():
       if k == 1447:
         continue
       phy_y0[k] += train_data[k]
       nspam_tot_w += train_data[k]
     y0 = y0+1 
   train_data = {}
 print nspam_tot_w, spam_tot_w
 phy_y1 = {k: v+1 /float(spam_tot_w + 1447) for k, v in phy_y1.iteritems()}
 phy_y0 = {k: v+1 /float(nspam_tot_w + 1447) for k, v in phy_y0.iteritems()}

 py1 = float(y1) / (y1 + y0)
 py0 = float(y0) / (y1 + y0)
 print py0, py1
 
 # Loading and testing data
 print "Testing........."
 count = 0
 crct = 0
 f = open("../spam_train_trial.txt")
 res1, res0, pred1, pred0 = 1,1,1,1;
 for line in f:
   count = count + 1
   test_data = parse_data(line)
   for k in test_data.iterkeys():
      #print k
      if k == 1447:
        continue
      res1 = res1 * test_data[k] * phy_y1[k]
      res0 = res0 * test_data[k] * phy_y0[k]
   #print res1, res0
   pred1 = (res1 * py1)/((res0 * py0)+(res1 * py1))
   pred0 = (res0 * py0)/((res0 * py0)+(res1 * py1))
   #print res1 , res0,  (res1 * py1),((res0 * py0)+(res1 * py1))
   if(pred1 > pred0 and test_data[1447] == 1) or ( pred1 < pred0 and test_data[1447] == 0):
     crct = crct + 1;
   #  print "******* Correct ********"
   print 'pred0:', pred0, "pred1:", pred1, " ; act" , test_data[1447]
   res ,res1, res0 =1, 1, 1
   #break
 acc = float(crct * 100) / count
 print "acc" , acc
