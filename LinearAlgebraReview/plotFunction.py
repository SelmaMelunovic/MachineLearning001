from matrixFunctions import *
import matplotlib.pyplot as plt

def least_squares(x,y):
    A =[[xi, 1] for xi in x]
    b = [[yi] for yi in y]

    At = trans(A)
    AtA = mul(At, A)
    Atb = mul(At,b)
    params = mul(inverse(AtA), Atb)

    m = params[0][0]
    b_val = params[1][0]

    plt.scatter(x,y, color = 'red', label = 'data points')
    x_line = [min(x), max(x)]
    y_line = [m * xi + b_val for xi in x_line]
    plt.plot(x_line, y_line, color = 'blue', label= f'y = {m:.2f}x + {b_val:.2f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Least Squares Fit')
    plt.legend()
    plt.show()

    return m, b_val

x = [1,2,3,4]
y = [2,5,3,8]
m, b = least_squares(x,y)
print(f"Slope: {m:.2f}, Intercept: {b:.2f}")
