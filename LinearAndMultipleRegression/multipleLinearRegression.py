from linearRegression import *
#In real life, price depends on more than just size.
#ŷ = w0 + w1*Size + w2*Bedrooms + w3*Bathrooms + w4*Age + w5*Distance

#Prediction for one row function

def predict_row(w, x_row):
    y_pred = w[0]
    for j in range(len(x_row)):
        y_pred += w[j + 1] * x_row[j]
    return y_pred

#Cost Function using predict_row

def muli_linear_reg_cost(w, x, y):
    m = len(x)
    total_error = 0
    for i in range(m):
        y_pred = predict_row(w, x[i])
        error = y_pred - y[i]
        total_error += error ** 2
    return total_error / (2 * m)

#Gradient
#∂J/∂w0 = (1/m) Σ (ŷ(i) - y(i))
#∂J/∂wj = (1/m) Σ (ŷ(i) - y(i)) * xj(i)   for j = 1..n

def multi_linear_reg_delta_cost(w, x, y):
    m = len(x)
    n = len(x[0])
    gradients = [0] * (n + 1)

    for i in range(m):
        y_pred = predict_row(w, x[i])
        error = y_pred - y[i]

        gradients[0] += error
        for j in range(n):
            gradients[j + 1] += error * x[i][j]

    for j in range(n + 1):
        gradients[j] /= m

    return gradients

#Training -> Same loop as before, but now we update a whole list of weights instead of just two.

def train_multi_linear_reg(x,
                           y,
                           learning_rate=0.00000001,
                           num_iterations=1000,
                           logging=False
                           ):
    n = len(x[0])
    w = [0] * (n + 1)

    for iteration in range(num_iterations):
        gradients = multi_linear_reg_delta_cost(w, x, y)
        for j in range(len(w)):
            w[j] = w[j] - learning_rate * gradients[j]
        if logging and iteration % 100 == 0:
            print(f"Iteration {iteration}: weights = {[round(x,4) for x in w]}")

    return w


#Testing
x_multi = [row[:-1] for row in data]
y = column(data, -1)

w = train_multi_linear_reg(x_multi, y, learning_rate=0.00000001, num_iterations=2000, logging=True)

y_pred = [predict_row(w, x_multi[i]) for i in range(len(x_multi))]
for i in range(5):
    print(f"Real: {y[i]:,.0f}   Predicted: {y_pred[i]:,.0f}")
