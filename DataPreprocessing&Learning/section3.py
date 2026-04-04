from section1 import *
from section2 import *

#DATA PROCESSING

def replace_null_values(data, index, replace_value=0):
    for row in data:
        if row[index] == '' or row[index] is None:
            row[index] = replace_value
    return data

def encoding(data, index):
    mapping = {"Iris-setosa": 0, "Iris-versicolor": 0.5, "Iris-virginica": 1}
    for row in data:
        row[index] = mapping[row[index]]
    return data

def min_max_scaling(data, index):
    min_val, max_val = min_max(data, index)
    for row in data:
        if isinstance(row[index], float):
            row[index] = (row[index] - min_val) / (max_val - min_val)
    return data

def normalize(data, index, decimals=2):
    m = mean(data, index)
    d = std_dev(data, index)
    for row in data:
        if  isinstance(row[index], float):
            row[index] = round((row[index] -m) / d, decimals)
    return data

#mean_col1 = mean(data, 1)
#mean_col2 = mean(data, 2)
#mean_col3 = mean(data, 3)
#mean_col4 = mean(data, 4)

#data = replace_null_values(data, 1, mean_col1)
#data = replace_null_values(data, 2, mean_col2)
#data = replace_null_values(data, 3, mean_col3)
#data = replace_null_values(data, 4, mean_col4)
#data = encoding(data, 5)
#data = min_max_scaling(data, 1)
data = normalize(data, 1)
print(data[:1])