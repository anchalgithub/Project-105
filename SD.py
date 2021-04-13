print("Hello!")
print("This is the standard deviation of the file 'data.csv'.")
import csv
import math 
with open('data.csv', newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)
    data=fileData[0]
    

def mean(data):
    n = len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean

squareList=[]
for number in data:
    a = int(number) -mean(data)
    a=a**2
    squareList.append(a)

sum=0
for i in squareList:
    sum=sum+i
result=sum/(len(data)-1)
standardD=math.sqrt(result)
print(standardD)