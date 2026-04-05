from gradientDescent import *

import matplotlib.pyplot as plt

learning_rates = [0.01, 0.1, 0.5]
num_iterations = 50

for lr in learning_rates:
    x = 3
    costs = []

    for i in range(num_iterations):
        costs.append(cost_function(x))
        x = x -lr * gradient_function(x)

    plt.plot(costs, label=f"lr = {lr}")

plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.title("Gradient Descent - Cost at Different Learning Rates")
plt.legend()
plt.show()