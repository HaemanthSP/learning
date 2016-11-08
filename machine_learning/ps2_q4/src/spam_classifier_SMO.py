import numpy as np
import random

def parse_data(data_path,data,y):
 f = open(data_path)
 for i,line in enumerate(f):
   for x in line.split(", "):
     if int(x.split(" ")[0]) == 1447:
       y[i] = int(x.split(" ")[1])
       continue
     data[i][int(x.split(" ")[0])] = int(x.split(" ")[1])
 return data, y

tol = 0.001
max_passes = 10
passes = 0
m = 1000 
b = 0 
C = 100 
alpha = np.zeros(m)
alpha_old = np.zeros(m)
X = np.zeros((m,1447))
y = np.zeros((m))

# Training
print  "Training......"
train_dpath = "../test_trial_smo.txt"
X, y = parse_data(train_dpath,X, y)
pred = 0
while passes < max_passes:
  num_changed_alphas = 0
  for i in range(m):
    pred = b
    for j in range(m):
      pred = pred + (alpha[j]*y[j]* np.dot(X[j].T,X[i]))
    if pred >= 0:
      pred = 1
    else:
      pred = -1
    #pred = alpha[i] * y[i] * np.dot(X[i].T,X[0]) + b
    #if pred >= 0:
    #  pred = 1
    #else:
    #  pred = -1

    Ei = pred - y[i]
    if ((y[i]*Ei < -tol) and (alpha[i] < C)) or ((y[i]*Ei > tol) and (alpha[i] > 0)):
      while 1:
       j  = random.randint(0,m-1)
       if i != j:
	 break
      alpha_old[i] = alpha[i]
      alpha_old[j] = alpha[j]
     
      if y[i] != y[j]:
        L = max(0, alpha[j] - alpha[i])
        H = min(C, C + alpha[j] - alpha[i])
      else:
        L = max(0, alpha[i] + alpha[j] - C)
        H = min(C, alpha[i] + alpha[j])

      if L == H:
        continue
      eta = 2 * np.dot(X[i].T, X[j]) - np.dot(X[i].T, X[i]) - np.dot(X[j].T, X[j])
      if eta >= 0:
        continue

      pred = alpha[j] * y[j] * np.dot(X[j].T,X[0]) + b
      if pred >= 0:
        pred = 1
      else:
        pred = -1

      Ej = pred - y[j]
      alpha[j] = alpha[j] - ((y[j] * (Ei - Ej))/ eta)
      
      if alpha[j] > H:
	alpha[j] = H
 
      if alpha[j] < L:
	alpha[j] = L

      if abs(alpha[j] - alpha_old[j]) < 0.00001:
	continue

      alpha[i] = alpha[i] + y[i] * y[j] * (alpha_old[j] - alpha[j])

      b1 = b - Ei - y[i] * (alpha[i] - alpha_old[i]) * np.dot(X[i], X[i])\
	 	  - y[j] * (alpha[j] - alpha_old[j]) * np.dot(X[i], X[j])
      b2 = b - Ei - y[i] * (alpha[i] - alpha_old[i]) * np.dot(X[i], X[j])\
		  - y[j] * (alpha[j] - alpha_old[j]) * np.dot(X[j], X[j])

      if (alpha[i] < 0) and (alpha[i] > C):
	b = b1
      elif alpha[j] < 0 and alpha[j] > C:
 	b = b2
      else:
	b = (b1+b2)/2
      num_changed_alphas = num_changed_alphas + 1
  if num_changed_alphas == 0:
    passes = passes + 1
    print "Passes" , passes
  else:
    print "Passes" , passes
    passes = 0
print alpha

print "Testing..."
test_X = np.zeros((m,1447))
test_y = np.zeros((m))

test_dpath = "../train_trial_smo.txt"
test_X, test_y = parse_data(test_dpath, test_X, test_y)

count = 0
total = 0
for i, teX in enumerate(test_X):
 cumm = b
 for j, trX in enumerate(X):
   cumm = cumm + (alpha[j]*y[j]* np.dot(trX.T,teX))
 if cumm >= 0:
   pred = 1
 else:
   pred = -1

 if pred == test_y[i]:
  count = count + 1

 total = total + 1
acc = float(count*100) / total 
print acc, np.shape(test_X)
