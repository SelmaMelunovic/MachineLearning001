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
| 4 | Lab 4 | Coming soon... | 🔄 In Progress |

---

## 📁 Project Structure
```
MachineLearning1/
│
├── .venv/
├── DataPreprocessing&Learning/
│   ├── __init__.py
│   ├── Iris.csv
│   ├── output.csv
│   ├── section1.py
│   ├── section2.py
│   ├── section3.py
│   └── section4.py
├── GradientDecentAlgorithm/
│   ├── __init__.py
│   ├── gradientDescent.py
│   └── visual.py
├── LinearAlgebraReview/
│   ├── __init__.py
│   ├── matrixFunctions.py
│   └── plotFunction.py
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
