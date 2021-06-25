import math
import csv

with open('data.csv', newline='') as a:
    reader = csv.reader(a)
    file_data = list(reader)
data = file_data.pop(0)
m = len(data)

def mean(data):
    
    total = 0
    for x in data:
        total += int(x)
    mean = total/m
    return mean

square_list = []
for number in data:
    d = int(number) - mean(data)
    d = d**2
    square_list.append(d)

sum = 0
for i in square_list:
    sum += i

result = sum/(m-1)

std_dev = math.sqrt(result)

print(std_dev)