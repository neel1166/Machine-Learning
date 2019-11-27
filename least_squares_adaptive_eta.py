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

stop_con=0.001
# w intitalization
w = [(0.02 * r.random())-0.01 for i in range(cols)]

converged=False
while not converged:
	derv_f=[0]*(cols)
	for i in range(rows):
		if( train_lab.get(i)!=None):
			wt= sum([a*b for a,b in zip(w,data[i])])
			temp=[(train_lab[i]-wt)*data[i][j] for j in range(cols)]
			derv_f=[a+b for a,b in zip(derv_f,temp)]

	eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001,.00000000001]
	bestobj = 1000000000000
	for eta in eta_list:
	
		w=[(w[i] + eta* derv_f[i]) for i in range(cols)]
		
		error = 0
		for i in range(0,rows,1):
			if (train_lab.get(i) != None):
				error += (train_lab[i] - sum([a*b for a,b in zip(w,data[i])]))**2

		obj=error
		if(obj < bestobj):
			best_eta = eta
			bestobj = obj

		w=[(w[i] - eta* derv_f[i]) for i in range(cols)]

	print("Best eta: ",best_eta)
	eta=best_eta

### Updating w  
	w=[(w[i] + eta* derv_f[i]) for i in range(cols)]
	

### updating cost function and convergence check
	cost_fun=0
	for i in range(rows):
		if( train_lab.get(i)!=None):
			cost_fun += (train_lab[i] - sum([a*b for a,b in zip(w,data[i])]))**2
	if(abs(error-cost_fun)<=stop_con):
		converged=True
	#print(cost_fun)
	error=cost_fun

print('Printing all w:')
for i in w[:-1]:
	#print(i)
 

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