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

rows=len(data)
cols=len(data[0])

clust_num = int(sys.argv[2])

##### Calculating K-mean
col = [0] * cols
euc_dist = col * clust_num

for i in range(clust_num):
    value = random.randrange(1, rows-1)
    euc_dist[i] = data[value]
cluster = {}

prev = [[0]*cols for i in range(clust_num)]

clust_element = [0] * clust_num

clust_dist = 1

while ((clust_dist) > 0):
    for i in range(0, rows, 1):
        distance = []

        for k in range(clust_num):
            distance.append(0)

        for k in range(clust_num):
            for j in range(0, cols, 1):
                distance[k] += ((data[i][j] - euc_dist[k][j])**2)
            distance[k] = (distance[k])**0.5

        mindist = 0
        mindist = min(distance)
        for k in range(clust_num):
            if(distance[k] == mindist):
                cluster[i] = k
                clust_element[k] += 1
                break

    euc_dist = [[0]*cols for i in range(clust_num)]
    col = []

    for i in range(0, rows, 1):
        for k in range(clust_num):
            if(cluster.get(i) == k):
                for j in range(0, cols, 1):
                    dist = euc_dist[k][j]
                    point = data[i][j]
                    euc_dist[k][j] = dist + point
    for j in range(0, cols, 1):
        for i in range(clust_num):
            euc_dist[i][j] = euc_dist[i][j]/clust_element[i]

    clust_element = [0.1]*clust_num

    temp_dist = []
    for i in range(clust_num):
        temp_dist.append(0)
    for i in range(clust_num):
        for c in range(0, cols, 1):
            temp_dist[i] += float((prev[i][c]-euc_dist[i][c])**2)

        temp_dist[i] = (temp_dist[i])**0.5

    prev = euc_dist
    clust_dist = 0
    for i in (temp_dist):
        clust_dist += i

for i in range(rows):
    print(cluster[i], i)