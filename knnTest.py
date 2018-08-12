import xlrd
import xlsxwriter
import math

file_loc = "Dataset.xlsx"
wkb = xlrd.open_workbook(file_loc)
sheetTrain = wkb.sheet_by_index(0)
sheetTest = wkb.sheet_by_index(1)

k = 49

dataTrain = []
dataTest = []

for row in range (1,4001):
    _row = []
    for col in range (sheetTrain.ncols):
        _row.append(sheetTrain.cell_value(row,col))
    dataTrain.append(_row)

for row in range (1,1001):
    _row = []
    for col in range (sheetTest.ncols):
        _row.append(sheetTest.cell_value(row,col))
    dataTest.append(_row)

def similarity(L1, P1, K1, E1, L2, P2, K2, E2):
    hasil = (L1-L2)**2 + (P1-P2)**2 + (K1-K2)**2 + (E1-E2)**2
    return math.sqrt(hasil)

result = []
distance = []
def knn(k,Train,Test):
    for i in range (0,1000):
        yes = 0
        no  = 0
        for j in range (0,4000):
            temp = similarity(Test[i][1],Test[i][2],Test[i][3],Test[i][4],Train[j][1],Train[j][2],Train[j][3],Train[j][4])
            distance.append([temp,Train[j][5]])
        distance.sort()
        for l in range(0,k):
            if distance[l][1] == 1.0:
                yes += 1
            else:
                no += 1
        if yes > no:
            result.append([Test[i][0],Test[i][1],Test[i][2],Test[i][3],Test[i][4],1.0])
        else:
            result.append([Test[i][0],Test[i][1],Test[i][2],Test[i][3],Test[i][4],0.0])
        print("Classification data-",i)
        distance.clear()

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
def assignToExcel(data):
    workbook = xlsxwriter.Workbook('Result.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(len(data)):
        rowA = A + str(i+2)
        rowB = B + str(i+2)
        rowC = C + str(i+2)
        rowD = D + str(i+2)
        rowE = E + str(i+2)
        rowF = F + str(i+2)
        worksheet.write(rowA,data[i][0])
        worksheet.write(rowB,data[i][1])
        worksheet.write(rowC,data[i][2])
        worksheet.write(rowD,data[i][3])
        worksheet.write(rowE,data[i][4])
        worksheet.write(rowF,data[i][5])
    workbook.close()

knn(k,dataTrain,dataTest)
assignToExcel(result)