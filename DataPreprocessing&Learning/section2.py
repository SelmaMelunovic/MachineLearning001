from section1 import *

#DATASET ANALYSIS

def mean(data, index):
    values = [row[index] for row in data if isinstance(row[index], float)]
    return sum(values) / len(values)

def std_dev(data, index):
    values = [row[index] for row in data if isinstance(row[index], float)]
    m = sum(values) / len(values)
    total = sum((v - m)** 2 for v in values)
    return (total / len(values)) ** 0.5

def variance(data, index):
    values = [row[index] for row in data if isinstance(row[index], float)]
    m = sum(values) / len(values)
    total = sum ((v - m)** 2 for v in values)
    return total / len(values)

def min_max(data, index):
    values = [row[index] for row in data if isinstance(row[index], float)]
    return min(values), max(values)

data = read_file('Iris.csv')
result = mean(data, 2)
print(result)

something = std_dev(data, 2)
print(something)

var = variance(data, 2)
print(var)

minmax = min_max(data, 2)
print(minmax)





