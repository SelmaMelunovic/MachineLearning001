from linearRegression import *
from multipleLinearRegression import *

#matrix helpers

def mat_vec_mul(x,w):
    """X (m×k) · w (k,) → result (m,)"""
    m = len(x)
    result = [0.0] * m
    for i in range(m):
        for j in range(len(w)):
            result[i] += x[i][j] * w[j]
    return result

def vec_sub(a,b):
    return [a[i] - b[i] for i in range(len(a))]

def dot(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))
def mat_T_vec_mul(x, e):
    """Xᵀ (k×m) · e (m,) → result (k,)"""
    k = len(x[0])
    result = [0.0] * k
    for i in range(len(x)):
        for j in range(k):
            result[j] += x[i][j] * e[i]
    return result

#Vectorized Cost

def linear_reg_cost_vec(w, x, y):
    m = len(y)
    y_hat = mat_vec_mul(x, w)
    e = vec_sub(y_hat, y)
    return dot(e, e) / (2 * m)

#Vectorized gradient

def linear_reg_delta_cost_vec(w, x, y):
    m = len(y)
    y_hat = mat_vec_mul(x, w)
    e = vec_sub(y_hat, y)
    grad = mat_T_vec_mul(x, e)
    return [g / m for g in grad]

#Vectorized training

def train_linear_reg_vec(x,
                         y,
                         w,
                         learning_rate = 0.00000001,
                         num_iterations=1000,
                         logging = True
                         ):
    for iteration in range(num_iterations):
        grad = linear_reg_delta_cost_vec(w, x, y)
        w = [w[j] - learning_rate * grad[j] for j in range(len(w))]
        if logging and iteration % 100 == 0:
            cost = linear_reg_cost_vec(w, x, y)
            print(f"Iteration: {iteration} Cost: {cost:.2f}")

    final_cost = linear_reg_cost_vec(w, x, y)
    return w, final_cost

#TESTING

x_raw = column(data, 0)
y = column(data, -1)

x_vec = [[1,x] for x in x_raw]
w = [0.0, 0.0]

w, final_cost = train_linear_reg_vec(x_vec,
                                     y,
                                     w,
                                     learning_rate = 0.00000001,
                                     num_iterations = 10000,
                                     logging = True)
y_pred = [w[0] + w[1] * x for x in x_raw]
print(f"Learned: w0={w[0]:.2f}, w1={w[1]:.4f}, final cost={final_cost:.2f}")

