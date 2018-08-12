import xlrd
import math

file_loc = "Dataset.xlsx"
wkb = xlrd.open_workbook(file_loc)
sheet = wkb.sheet_by_index(0)
k = 49#change this variable's value for more optimum accuracy

dataTrain = []
dataTest = []

for row in range (1,3001):#load data 1 to 3000 for data train
    _row = []
    for col in range (sheet.ncols):
        _row.append(sheet.cell_value(row,col))
    dataTrain.append(_row)

for row in range (3001,4001):#load data 3001 to 4000 for data test
    _row = []
    for col in range (sheet.ncols):
        _row.append(sheet.cell_value(row,col))
    dataTest.append(_row)

def similarity(L1, P1, K1, E1, L2, P2, K2, E2):#function for count the distance between data
    hasil = (L1-L2)**2 + (P1-P2)**2 + (K1-K2)**2 + (E1-E2)**2
    return math.sqrt(hasil)

result = []
distance = []
def knn(k,Train,Test):#function for implementation k-Nearest Neighbour algorithm
    for i in range (0,1000):
        yes = 0
        no  = 0
        for j in range (0,3000):
            temp = similarity(Test[i][1],Test[i][2],Test[i][3],Test[i][4],Train[j][1],Train[j][2],Train[j][3],Train[j][4])
            distance.append([temp,Train[j][5]])
        distance.sort()
        for l in range(0,k):
            if distance[l][1] == 1.0:
                yes += 1
            else:
                no += 1
        if yes > no:
            result.append(1.0)
        else:
            result.append(0.0)
        print("Count distance data-",i+1)
        distance.clear()

#code below are the code to call all function already made
knn(k,dataTrain,dataTest)
temp = 0
for m in range(0,1000):
    if result[m] == dataTest[m][5]:
        temp += 1
print("  ")
print("Accuracy : ",temp/1000*100,"%")