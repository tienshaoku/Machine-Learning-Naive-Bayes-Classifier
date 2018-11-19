import numpy as np
import pprint

I = 100
J = 1000
K = 10000

x_tr= np.load('x_train.npy')
y_tr= np.load('y_train.npy')
x_te= np.load('x_test.npy')
y_te= np.load('y_test.npy')

dic={}
for col in range(len(x_tr)):
    for word in set(x_tr[col]):
        try:
            dic[word]
        except:
            dic[word] = np.zeros((2, 3))

        dic[word][0, 2] += 1
        if y_tr[col]==1:
            dic[word][0, 0] +=1
        else:
                
            dic[word][0, 1] +=1
         
# P(positive|given text)= P(positive)* P(positive, given text)/ P(given text)
 
commits = np.zeros(2)
for commit in y_tr:
    if commit:
        commits[0] += 1
    else:
        commits[1] += 1

for item in dic:
    dic[item][1,0]= commits[0]- dic[item][0,0]
    dic[item][1,1]= commits[1]- dic[item][0,1]
    dic[item][1,2]= dic[item][1,0]+ dic[item][1,1]
    dic[item][:2, :2] /= commits
    dic[item][:2, 2] /= commits.sum()
commits /= commits.sum()

"""
print dic[1]
print dic[34]
print dic[223]
print dic[9999]
"""


arr100=[0]* len(x_te)
arr1000=arr100
arr10000=arr100
num=0
for art in x_te:
    pos_prob=1.0
    neg_prob=1.0
    for j in range(1,I+1):
        if j in art:
            pos_prob*= dic[j][0,0] 
            pos_prob/= dic[j][0,2]
            neg_prob*= dic[j][0,1]
            neg_prob/= dic[j][0,2]
        else:
            pos_prob*= dic[j][1,0]
            pos_prob/= dic[j][1,2]
            neg_prob*= dic[j][1,1]
            neg_prob/= dic[j][1,2]
    pos_prob*= commits[0] 
    neg_prob*= commits[1]
    if pos_prob>= neg_prob:
        arr100[num]=1
    else:
        arr100[num]=0
    num+=1

tp100=0.0
fn100=0.0
fp100=0.0
tn100=0.0
for i in range(len(arr100)):
    if arr100[i]== y_te[i] & y_te[i]==1:
        tp100+=1
    elif arr100[i]== y_te[i] & y_te[i]==0:
        tn100+=1
    elif arr100[i]!= y_te[i] & y_te[i]==1:
        fn100+=1
    else:
        fp100+=1
#print tp100
#print fn100
#print fp100
#print tn100
acc100= (tp100+tn100) / (tp100+fn100+tn100+fp100)
pre100= tp100/ (tp100+fp100)
re100= tp100/ (tp100+fn100)
print "accuracy of K=100 is:", acc100
print "precision of K=100 is:", pre100
print "recall of K=100 is:", re100

num=0
for art in x_te:
    pos_prob=1.0
    neg_prob=1.0
    for j in range(1,J+1):
        if j in art:
            pos_prob*= dic[j][0,0]
            pos_prob/= dic[j][0,2]
            neg_prob*= dic[j][0,1]
            neg_prob/= dic[j][0,2]
        else:
            pos_prob*= dic[j][1,0]
            pos_prob/= dic[j][1,2]
            neg_prob*= dic[j][1,1]
            neg_prob/= dic[j][1,2]
    pos_prob*= commits[0]
    neg_prob*=commits[1]
    if pos_prob>= neg_prob:
        arr1000[num]=1
    else:
        arr1000[num]=0
    num+=1

tp1000=0.0
fn1000=0.0
fp1000=0.0
tn1000=0.0
for i in range(len(arr1000)):
    if arr1000[i]== y_te[i] & y_te[i]==1:
        tp1000+=1
    elif arr1000[i]== y_te[i] & y_te[i]==0:
        tn1000+=1
    elif arr1000[i]!= y_te[i] & y_te[i]==1:
        fn1000+=1
    else:
        fp1000+=1
#print tp1000
#print fn1000
#print fp1000
#print tn1000
acc1000= (tp1000+tn1000) / (tp1000+fn1000+tn1000+fp1000)
pre1000= tp1000/ (tp1000+fp1000)
re1000= tp1000/ (tp1000+fn1000)
print "accuracy of K=1000 is:", acc1000
print "precision of K=1000 is:", pre1000
print "recall of K=1000 is:", re1000



num=0
for art in x_te:
    pos_prob=1.0
    neg_prob=1.0
    for j in range(1,K+1):
        if j in art:
            pos_prob*= dic[j][0,0]
            pos_prob/= dic[j][0,2]
            neg_prob*= dic[j][0,1]
            neg_prob/= dic[j][0,2]
        else:
            pos_prob*= dic[j][1,0]
            pos_prob/= dic[j][1,2]
            neg_prob*= dic[j][1,1]
            neg_prob/= dic[j][1,2]
    pos_prob*= commits[0]
    neg_prob*=commits[1]
    if pos_prob>= neg_prob:
        arr10000[num]=1
    else:
        arr10000[num]=0
    num+=1

tp10000=0.0
fn10000=0.0
fp10000=0.0
tn10000=0.0
for i in range(len(arr10000)):
    if arr10000[i]== y_te[i] & y_te[i]==1:
        tp10000+=1
    elif arr10000[i]== y_te[i] & y_te[i]==0:
        tn10000+=1
    elif arr10000[i]!= y_te[i] & y_te[i]==1:
        fn10000+=1
    else:
        fp10000+=1
#print tp10000
#print fn10000
#print fp10000
#print tn10000
acc10000= (tp10000+tn10000) / (tp10000+fn10000+tn10000+fp10000)
pre10000= tp10000/ (tp10000+fp10000)
re10000= tp10000/ (tp10000+fn10000)
print "accuracy of K=10000 is:", acc10000
print "precision of K=10000 is:", pre10000
print "recall of K=10000 is:", re10000
