
# Cost Function

def cost_function(x):
    return x**2 + 4*x + 2

# Gradient function -> first derivative of the cost function

def gradient_function(x):
    return 2*x + 4

# Gradient Descent -> the main algorithm

def gradient_descent(cost_function, gradient_function, initial_x, learning_rate, num_iterations, logging = False):
    x = initial_x

    for i in range(num_iterations):
        y = cost_function(x)
        gradient = gradient_function(x)
        x = x -learning_rate * gradient

        if logging:
            print(f"Iteration {i+1}: x = {x}, cost = {cost_function(x)}")

    return x, cost_function(x)

optimized_x, final_cost = gradient_descent(
    cost_function,
    gradient_function,
    initial_x=3,
    learning_rate=0.1,
    num_iterations=100,
    logging=True
)

fun = cost_function(10)
print(fun)

fun1 = gradient_function(10)
print(fun1)

print(f"\nOptimized x: {optimized_x}")
print(f"Final cost: {final_cost}")
