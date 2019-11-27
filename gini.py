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

#### Calculating Gini Index

gini_values=[[0,0]]*cols

for j in range(0,cols, 1):

    listcol = [item[j] for item in data]
    keys = sorted(range(len(listcol)), key=lambda k: listcol[k])
    listcol.sort()
    ginival = []
    prevgini = 0
    prevrow = 0
    for k in range(1, rows, 1):

        lsize = k
        rsize = rows - k
        lp,rp=0,0

        for l in range(0, k, 1):
            if (train_lab.get(keys[l]) == 0):
                lp+=1
        for r in range(k, rows, 1):
            if (train_lab.get(keys[r]) == 0):
                rp+=1
        gini = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + (rsize / rows) * (rp / rsize) * (1 - rp / rsize)
        ginival.append(gini)

        prevgini = min(ginival)
        if (ginival[k - 1] == float(prevgini)):
            gini_values[j][0] = ginival[k - 1]
            gini_values[j][1] = k
    if (j == 0):
        index = gini_values[j][0]

    if (gini_values[j][0] <= index):
        index = gini_values[j][0]
        col = j
        split = gini_values[j][1]
        if (split != 0):
            split = (listcol[split] + listcol[split - 1]) / 2
print("gini:", index)
print("column number:",col)
print("split:",split)