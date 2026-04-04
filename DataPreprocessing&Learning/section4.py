from section1 import *
from section3 import *

import matplotlib.pyplot as plt

def plot(labels, values, type='hist'):
    if type == 'hist':
        plt.hist(values)
    elif type == 'bar':
        plt.bar(labels, values)
    elif type == 'pie':
        plt.pie(values, labels=labels)
    plt.title(type)
    plt.show()


#HIST
values = [row[1] for row in data if isinstance(row[1], float)]
plot([], values, type='hist')

#PIE
labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
values = [50, 50, 50]  # each species has 50 samples
plot(labels, values, type='pie')

#BAR
labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
values = [50, 50, 50]

plot(labels, values, type='bar')