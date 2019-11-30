import sys
import array
import math
import time
import random
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

start = time.time()

###########Reading Data and Labels

print('\n Reading Training Data')
try:
    data_file= open(sys.argv[1],'r')
except FileNotFoundError:
    print('\n Please provide the correct Training Data filename/Filepath')
    sys.exit()
data=[] # list of data
for l in data_file:
    data.append(array.array('i',map(int,l.split())))

print('\n Reading training labels')

labelfile =sys.argv[2]
trainlabels = array.array("i")
with open(labelfile, "r") as infile:
    for line in infile:
        l= line.split()
        trainlabels.append(int(l[0]))
print('\nDone Reading Training Labels')

##### Feature Selection
print('\n Calculating Pearson Correlation Coeffiecient')
rows = len(data)
cols = len(data[0])

pcc = array.array('f')

for c in range(cols):
    XY = 0
    X, Y = 0, 0
    X2, Y2 = 0, 0
    for r in range(rows):
        XY += data[r][c] * trainlabels[r]
        X += data[r][c]
        Y += trainlabels[r]
        X2 += data[r][c] ** 2
        Y2 += trainlabels[r] ** 2
    p = (rows * XY - X * Y) / math.sqrt((rows * X2 - (X ** 2)) * (rows * Y2 - (Y ** 2)))
    pcc.append(abs(p))
print('Done with Calculating Pearson Correlation Coeffiecient')



pcc_index = sorted(range(len(pcc)), key=lambda i: pcc[i])[-25:] # Extracter feature indices ( 25 features )
new_features=[]
for d in data:
    new_features.append([d[index]for index in pcc_index])

print('\n Started Classifying Training Dataset')
newtrain,validation,newlabels,validationlabels= train_test_split(new_features, trainlabels, test_size=0.2, random_state=42)

clf_svm = svm.SVC(gamma='auto')
clf_svm.fit(newtrain, newlabels)
clf_lgr= LogisticRegression()
clf_lgr.fit(newtrain, newlabels)
clf_km=KNeighborsClassifier()
clf_km.fit(newtrain,newlabels)
clf_gnb= GaussianNB()
clf_gnb.fit(newtrain,newlabels)
prediction=[]
#prediction = clf.predict(validation)
accuracy=0
err = 0

for i in validation:
    svm_pred = int(clf_svm.predict([i]))
    lgr_pred = int(clf_lgr.predict([i]))
    km_pred = int(clf_km.predict([i]))
    gnb_pred = int(clf_gnb.predict([i]))
    list_pred =[svm_pred,km_pred,lgr_pred,gnb_pred]
    #print(list_pred)
    prediction.append(max(list_pred, key=list_pred.count))

for i in range(0, len(prediction), 1):
    if (prediction[i] == validationlabels[i]):
        accuracy += 1
acc_score = accuracy/len(validationlabels)

print('\n Done with Classifying Training Dataset')
print('\n Accuracy:',round(acc_score*100),'%')

####### Test Data Reading

print('\n Reading Test Data')
try:
    test_data_file= open(sys.argv[3],'r')
except FileNotFoundError:
    print('\n Please provide the correct Test Data filename/Filepath')
    sys.exit()
test_data=[] # list of test data
for l in test_data_file:
    test_data.append(array.array('i',map(int,l.split())))
print('\n Done Reading with Test Data')

print('\n Started Feature section over Test Data')
f1 = open("test_features", "w+")
test_data_features=[]
for d in test_data:
    test_data_features.append([d[index]for index in pcc_index])
for list in test_data_features:
    for ft in list:
        f1.write(str(ft)+" ")
    f1.write("\n")


    #f1.write(str(f).strip() + "\n")
f1.close()
print('\n Done with Feature section over Test Data')
print('\n Extracted Feature of test dataset is stored in "test_features" file')

print('\n Classifying Test Data')
f2 = open("test_labels", "w+")
for i in range(len(test_data_features)):
    svm_pred = int(clf_svm.predict([test_data_features[i]]))
    lgr_pred = int(clf_lgr.predict([test_data_features[i]]))
    km_pred = int(clf_km.predict([test_data_features[i]]))
    gnb_pred = int(clf_gnb.predict([test_data_features[i]]))
    list_pred =[svm_pred,km_pred,lgr_pred,gnb_pred]
    label = max(list_pred, key=list_pred.count)
    #print(str(label) + " " + str(i))
    f2.write(str(label) + " " + str(i) + "\n")
f2.close()
print('\n Done with Classifying Test Data')
print('\n Predicted labels of the test dataset are stored in "test_labels" file')

print("\nExecution time:", time.time() - start)
