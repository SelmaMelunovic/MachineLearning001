#Read function

def is_number(s):
    if s is None: return False
    try:
        complex(s)
    except ValueError:
        return False
    return True

def read_file(file_path):
    with open(file_path, 'r') as file:
        data =[]
        lines = file.readlines()
        for i in range(1, len(lines)):
            data_row = [
                float(cell.strip('\n')) if is_number(cell.strip('\n')) else cell.strip('\n')
                for cell in lines[i].split(',')
            ]
            data.append(data_row)
        return data

def column(matrix,i):
    return [row[i] for row in matrix]


#Cost function -> measuring for total errors
#J(w0, w1) = (1 / 2m) * Σ (ŷ(i) - y(i))²

def linear_reg_cost(w0, w1, x, y):
    m = len(x)
    total_error = 0
    for i in range(m):
        y_pred = w0 + w1 * x[i]
        error = y_pred - y[i]
        total_error += error ** 2
    return total_error / (2 * m)


#Gradient Delta Cost -> slope of the cost surface
#∂J/∂w0 = (1/m) * Σ (ŷ(i) - y(i))
#∂J/∂w1 = (1/m) * Σ (ŷ(i) - y(i)) * x(i)

def linear_reg_delta_cost(w0, w1, x, y):
    m = len(x)
    sum_w0 = 0
    sum_w1 = 0
    for i in range(m):
        y_pred = w0 + w1 * x[i]
        error = y_pred - y[i]
        sum_w0 += error
        sum_w1 += error * x[i]
    dw0 = sum_w0 / m
    dw1 = sum_w1 / m
    return dw0, dw1

#Training function -> Now we put it together. We start with w0 = 0, w1 = 0 (a flat, zero line) and iteratively nudge both weights in the direction that lowers the cost.
#w0 := w0 - α * ∂J/∂w0
#w1 := w1 - α * ∂J/∂w1

def train_linear_reg(x,
                     y,
                     w0 = 0,
                     w1 = 0,
                     learning_rate = 0.0000004,
                     num_iterations = 1000,
                     logging = False):
    for iteration in range(num_iterations):
        dw0, dw1 = linear_reg_delta_cost(w0,w1,x,y)
        w0 = w0 - learning_rate * dw0
        w1 = w1 - learning_rate * dw1
        if logging and iteration % 100 == 0:
            cost = linear_reg_cost(w0,w1,x,y)
            print(f"Iteration {iteration}, w0={w0:.2f}, w1={w1:.4f}, cost={cost:.2f}")
    return w0, w1


#TESTING
data = read_file('housing_data_5features.csv')

x = column(data,0)
y = column(data, -1)

w0, w1 = train_linear_reg(x, y, learning_rate=0.0000004, num_iterations=10000, logging=True)

y_pred = [w0 + w1 * x for x in x]

print(linear_reg_cost(0, 0, x, y))
print(linear_reg_delta_cost(0, 0, x, y))

print(f"Learned line: price = {w0:.0f} + {w1:.2f} * size")
for i in range(5):
    print(f"Real: {y[i]:,.0f}  Predicted: {y_pred[i]:,.0f}")




