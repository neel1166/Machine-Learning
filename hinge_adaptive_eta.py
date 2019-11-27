import sys
import math
import random as r

#####Data File
try:
    data_file= open(sys.argv[1],'r')
except FileNotFoundError:
    print('Please provide the correct Data filename/Filepath')
    sys.exit()
data=[] # list of data 
for l in data_file:
    data.append(list(map(float,l.split())))
for i in data:
	i.append(1)

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
    if (train_lab[int(a[1])] == 0):
            train_lab[int(a[1])] = -1
rows=len(data)
cols=len(data[0])


stop_con=.001
prev= 0
# w intitalization
w = [(0.02 * r.random())-0.01 for i in range(cols)]

Loss=True
while Loss:
	derv_f=[0]*(cols)
	for i in range(rows):
		if( train_lab.get(i)!=None):
			wt= sum([a*b for a,b in zip(w,data[i])])
			cd=train_lab.get(i) * wt
			for j in range(cols):
				if(cd < 1):
					derv_f[j] += -1 * (train_lab.get(i)*data[i][j])
				else:
					derv_f[j] += 0
	
	eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001,.00000000001]
	bestobj = 1000000000000
	for eta in eta_list:
	
		w=[(w[i] - eta* derv_f[i]) for i in range(cols)]
		
		error = 0
		for i in range(0,rows,1):
			if (train_lab.get(i) != None):
				error += max(0,1-(train_lab.get(i)* sum([a*b for a,b in zip(w,data[i])])))
		obj=error
		if(obj < bestobj):
			best_eta = eta
			bestobj = obj

		w=[(w[i] + eta* derv_f[i]) for i in range(cols)]

	print("Best eta: ",best_eta)
	eta=best_eta

### Updating w	
	w=[(w[i] - eta * derv_f[i]) for i in range(cols)]
	

### Hinge Loss evaluation
	h=[]
	for i in range(rows):
		if(train_lab.get(i)!=None):
			h.append(max(0,1-(train_lab.get(i)* sum([a*b for a,b in zip(w,data[i])]))))
	#print("Hinge Loss: ",sum(h))
	if(abs(prev-sum(h)) <= stop_con):
		Loss=False
	prev=sum(h)

#print('Printing all w:')
#print(i for i in w[:-1])
#print("w0: ",w[-1])

	
### calculating distance from origin
w0=math.sqrt(sum([i**2 for i in w[:-1]]))
dis_from_org=abs(w[-1]/w0)
#print(" Distance from origin : ",dis_from_org)

###Predicting labels
print("Predicted Labels :")
for i in range(rows):
	if(train_lab.get(i)==None):
		wt=sum([a*b for a,b in zip(w,data[i])])
		if wt > 0:
			print("1",i)
		else:
			print("0",i)