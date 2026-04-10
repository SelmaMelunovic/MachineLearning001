<div align="center">

# 🌸 Introduction to Machine Learning

### Lab Projects Repository

<br>

[![GitHub](https://img.shields.io/badge/GitHub-SelmaMelunovic-181717?style=for-the-badge&logo=github)](https://github.com/SelmaMelunovic)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Selma%20Melunović-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/selma-melunovi%C4%87-55b472361/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

</div>

---

## 👩‍💻 About Me

I am a **second-year university student** at **International Burch University** passionate about **Machine Learning and AI Engineering**.

This repository contains my lab implementations for the *"Introduction to Machine Learning"* course, which I will officially take in my third year. I am working through the labs **early out of personal interest** and will continue updating this repository as I progress.

> My goal is to implement everything **from scratch** so I truly understand what happens under the hood — not just how to call library functions.

---

## 📊 Current Progress

| # | Lab | Topic | Status |
|---|-----|-------|--------|
| 1 | Lab 1 | Data Preprocessing & Learning | ✅ Complete |
| 2 | Lab 2 | Gradient Descent Algorithm | ✅ Complete |
| 3 | Lab 3 | Linear Algebra Review | ✅ Complete |
| 4 | Lab 4 | Linear and Multiple Regression | ✅ Complete |
| 5 | Lab 5 | Coming soon... | 🔄 In Progress |

---

## 📁 Project Structure
```
MachineLearning1/
│
├── .venv/
├── DataPreprocessing&Learning/
│   ├── init.py
│   ├── Iris.csv
│   ├── output.csv
│   ├── section1.py
│   ├── section2.py
│   ├── section3.py
│   └── section4.py
├── GradientDecentAlgorithm/
│   ├── init.py
│   ├── gradientDescent.py
│   └── visual.py
├── LinearAlgebraReview/
│   ├── init.py
│   ├── matrixFunctions.py
│   └── plotFunction.py
├── LinearAndMultipleRegression/
│   ├── init.py
│   ├── housing_data_5features.csv
│   ├── linearRegression.py
│   ├── multipleLinearRegression.py
│   └── vectorizedRegression.py
├── main.py
└── README.md
```
---

## 🧪 Lab 1 - Data Preprocessing & Learning

### 📋 Dataset

The [IRIS dataset](https://www.kaggle.com/datasets/uciml/iris) contains **150 samples** of iris flowers across **3 species**.

| Column | Description | Type |
|--------|-------------|------|
| Id | Unique identifier | Numerical |
| SepalLengthCm | Length of the sepal (cm) | Numerical |
| SepalWidthCm | Width of the sepal (cm) | Numerical |
| PetalLengthCm | Length of the petal (cm) | Numerical |
| PetalWidthCm | Width of the petal (cm) | Numerical |
| Species | Iris-setosa / Iris-versicolor / Iris-virginica | Categorical |

#### ⚙️ What I Implemented

##### 📂 Section 1 - Read & Write
- `read_file()` — reads the IRIS dataset from a CSV file
- `write_data_to_file()` — saves processed data back to a CSV file

##### 📂 Section 2 - Dataset Analysis
- `mean()` — calculates the average of a selected column
- `std_dev()` — measures the spread of data
- `variance()` — measures the variability of data
- `min_max()` — finds the smallest and largest values in a column

##### 📂 Section 3 - Data Preprocessing
- `replace_null_values()` — fills missing values with the column mean
- `encoding()` — converts categorical Species column to numerical values
- `min_max_scaling()` — scales column values to range [0, 1]
- `normalize()` — applies Z-score standardization (mean=0, std=1)

##### 📂 Section 4 - Visualization
- Histogram — distribution before/after normalization
- Pie chart — equal distribution of Iris species
- Bar chart — compare discrete values

---

## 🧪 Lab 2 - Gradient Descent Algorithm

Gradient Descent is an optimization algorithm used to minimize a cost function by iteratively moving in the direction of steepest descent.

#### ⚙️ What I Implemented

- `cost_function()` — defines the cost function **x² + 4x + 2**
- `gradient_function()` — first derivative of the cost function **2x + 4**
- `gradient_descent()` — runs the algorithm with configurable learning rate and iterations
- Visualization of cost reduction at different learning rates

#### 💡 Key Concepts

| Concept | Description |
|---------|-------------|
| Learning Rate (α) | Controls the step size — too large overshoots, too small is slow |
| Starting Point | x = 3 |
| True Minimum | x = -2, cost = -2 |
| Cost Function | Must be differentiable and convex (f''(x) ≥ 0) |

---

## 🧪 Lab 3 - Linear Algebra Review

A complete implementation of matrix operations from scratch — no external libraries.

#### ⚙️ What I Implemented

- `size()` — returns number of rows and columns
- `generate()` — creates a matrix filled with a default value
- `scalar_mul()` — multiplies every element by a scalar
- `scalar_add()` — adds a scalar to every element
- `mul()` — matrix multiplication
- `concat()` — joins two matrices side by side
- `add()` / `sub()` — element-wise addition and subtraction
- `sum_el()` / `prod_el()` — sum and product of all elements
- `trans()` — matrix transpose
- `identity()` — generates the identity matrix
- `minor()` — removes a row and column from a matrix
- `cofactor()` — calculates the cofactor of an element
- `determinant()` — recursive determinant calculation
- `inverse()` — matrix inverse using adjugate method
- `least_squares()` — fits a line y=mx+b to data points and plots the result

---

## 🧪 Lab 4 - Linear and Multiple Regression

A complete implementation of linear regression from scratch — no external ML libraries. The goal is to understand how models learn by implementing the hypothesis function, cost function, and gradient descent manually.

### 📋 Dataset

The housing dataset contains **50 samples** of residential properties with **5 input features** and a target price.

| Column | Description | Type |
|--------|-------------|------|
| Size_sqm | Size of the house in square metres | Numerical |
| Bedrooms | Number of bedrooms | Numerical |
| Bathrooms | Number of bathrooms | Numerical |
| Age | Age of the house in years | Numerical |
| Distance | Distance to city centre (km) | Numerical |
| Price | Sale price in EUR (target) | Numerical |

#### ⚙️ What I Implemented

##### 📂 linearRegression.py — Simple Linear Regression
Predicts house price from a single feature (size).

- `linear_reg_cost()` — computes the Mean Squared Error (MSE) cost function
- `linear_reg_delta_cost()` — computes partial derivatives (gradients) w.r.t. w0 and w1
- `train_linear_reg()` — trains the model using Gradient Descent

##### 📂 multipleLinearRegression.py — Multiple Linear Regression
Extends the model to use all 5 features simultaneously.

- `predict_row()` — computes prediction for a single data point
- `multi_linear_reg_cost()` — MSE cost across all features
- `multi_linear_reg_delta_cost()` — gradients for all weights
- `train_multi_linear_reg()` — trains the model using Gradient Descent

##### 📂 vectorizedRegression.py — Vectorized Linear Regression
Reimplements the above using matrix algebra instead of explicit loops.

- `mat_vec_mul()` — matrix × vector multiplication (computes all predictions at once)
- `mat_T_vec_mul()` — transposed matrix × vector (computes all gradients at once)
- `linear_reg_cost_vec()` — vectorized MSE cost
- `linear_reg_delta_cost_vec()` — vectorized gradient
- `train_linear_reg_vec()` — vectorized training loop

#### 💡 Key Concepts

| Concept | Description |
|---------|-------------|
| Hypothesis | ŷ = w0 + w1·x1 + w2·x2 + ... + wn·xn |
| Cost Function | MSE = (1/2m) Σ (ŷ - y)² |
| Gradient Descent | w := w - α · ∂J/∂w |
| Learning Rate (α) | Too large → diverges, too small → slow convergence |
| Vectorization | Express all operations as matrix algebra for efficiency |

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/SelmaMelunovic/MachineLearning1
```

**2. Install dependencies**
```bash
pip install matplotlib
```

**3. Run the sections**
```bash
python section1.py
python section2.py
python section3.py
python section4.py
```

---

## 🔮 Future Plans

- [ ] Complete all remaining course labs
- [ ] Add more datasets
- [ ] Explore deep learning concepts
- [ ] Build real-world projects
- [ ] Start official course in Year 3 with a strong foundation

---

## 🛠️ Technologies

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)

---

<div align="center">

## 👩‍🎓 Author

**Selma Melunović**

*University Student | Year 2 of 3 | Aspiring ML & AI Engineer*

<br>

[![GitHub](https://img.shields.io/badge/GitHub-SelmaMelunovic-181717?style=for-the-badge&logo=github)](https://github.com/SelmaMelunovic)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Selma%20Melunović-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/selma-melunovi%C4%87-55b472361/)

<br>

⭐ *If you find this helpful, feel free to star the repository!* ⭐

</div>
