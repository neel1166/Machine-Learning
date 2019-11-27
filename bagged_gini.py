import sys
import random

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
def find_gini(data, labels, col_no):

    gini_values=[[0,0]]*cols

    #for j in range(0,cols, 1):

    listcol = [item[col_no] for item in data]
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
            if (labels[keys[l]] == 0):
                lp+=1
        for r in range(k, rows, 1):
            if (labels[keys[r]] == 0):
                rp+=1
        gini = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + (rsize / rows) * (rp / rsize) * (1 - rp / rsize)
        ginival.append(gini)

        prevgini = min(ginival)
        if (ginival[k - 1] == float(prevgini)):
            gini_values[col_no][0] = ginival[k - 1]
            gini_values[col_no][1] = k
    if (col_no == 0):
        index = gini_values[col_no][0]


    else:#if (gini_values[j][0] <= index):
        index = gini_values[col_no][0]
    col = col_no
    split = gini_values[col_no][1]
    if (split != 0):
        split = (listcol[split] + listcol[split - 1]) / 2
    return(split, index)
    # print("gini:", index)
    # print("column number:",col)
    # print("split:",split)

#Bagging Starts 

test_predictions = {}
for i in range(0, rows):
    if(train_lab.get(i) == None):
        test_predictions[i] = 0

for k in range(0, 100):
    i = 0
    bagged_data = []
    bagged_train_lab = {}
    while(i < len(data)):
        r = random.randint(0, rows-1)
        if(train_lab.get(r) != None):
            bagged_data.append(data[r])
            bagged_train_lab[i] = train_lab[r]
            i += 1

    best_split = -1
    best_col = -1
    best_gini = 100000
    for j in range(cols):
        [s, gini] = find_gini(bagged_data, bagged_train_lab, j)
        if(gini < best_gini):
            best_gini = gini
            best_split = s
            best_col = j
    print(best_gini,best_split,best_col)
    lab_0, lab_1 = 0, 0

    for i in range(rows):
        if(train_lab.get(i) != None):
            if(data[i][best_col] < best_split):
                if(train_lab[i] == 0):
                    lab_0 += 1
                else:
                    lab_1 += 1
    if(lab_0 > lab_1):
        left = -1
        right = 1
    else:
        left = 1
        right = -1

    for i in range(rows):
        if(train_lab.get(i) == None):
            if(data[i][best_col] < best_split):
                test_predictions[i] += left
            else:
                test_predictions[i] += right

for i in range(rows):
    if(train_lab.get(i) == None):
        if(test_predictions[i] > 0):
            print("1 ", i)
        else:
            print("0 ", i)