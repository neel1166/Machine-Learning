
######## Naive Bayes Classifier############

import sys

#####Data File
try:
	data_file= open(sys.argv[1],'r')
except FileNotFoundError:
	print('Please provide the correct Data filename/Filepath')
	sys.exit()
data=[] # list of data 
for l in data_file:
    data.append(list(map(float,l.split())))

#### training File

try:
	train_file= open(sys.argv[2],'r')
except FileNotFoundError:
	print('Please provide the correct Label Filename/Filepath')
	sys.exit()

train_lab={}
for l in train_file:
    a=l.split()
    train_lab[int(a[1])]=int(a[0])
rows=len(data)
cols=len(data[0])

###Reading Labels
lab_0,lab_1=[],[] # List of training Labels having result 0 and 1 
for a in train_lab:
    if train_lab[a]==0:
        lab_0.append(data[a])
    else:
        lab_1.append(data[a])



#### calculating Mean 

m0,m1=[],[] # List of mean 
v0,v1=[],[] # List of variance
for i in range(cols):
    sum=0
    for j in lab_0:
        sum+=j[i]
    m0.append(sum/len(lab_0))
    sum=0
    for j in lab_1:
        sum+=j[i]
    m1.append(sum/len(lab_1))

#### Calculating Variance
for i in range(cols):
	vr=0
	for j in lab_0:
		vr+= (j[i]- m0[i])**2
	if vr==0:
		for j in lab_0:
			vr+= (j[i]- (m0[i]+0.01/len(lab_0)))**2
	v0.append(vr/len(lab_0))
	vr=0
	for j in lab_1:
		vr+= (j[i]- m1[i])**2
	if vr==0:
		for j in lab_1:
			vr+= (j[i]- (m0[i]+0.01/len(lab_1)))**2
	v1.append(vr/len(lab_1))


### Label classification
for i in range(rows):
    if(train_lab.get(i)==None):
        t0,t1=0,0
        for j in range(cols):
            t0 +=((m0[j]-data[i][j])**2)/v0[j]
            t1 +=((m1[j]-data[i][j])**2)/v1[j]
        if(t0<t1):
            print("0",i)
        else:
            print("1",i)