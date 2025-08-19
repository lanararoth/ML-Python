import numpy as np
import matplotlib.pyplot as mpt

# Simple line graph y = x^2
x = np.linspace(-10, 10, 100)
y = x**2
mpt.plot(x, y, label="y = x²", color="blue")
mpt.title("Line Graph of y = x²")
mpt.xlabel("x")
mpt.ylabel("y")
mpt.legend()
mpt.show()

# Bar chart example
categories = ['A', 'B', 'C']
values = [10, 15, 7]
mpt.bar(categories, values, color='orange')
mpt.title("Bar Chart Example")
mpt.show()

# Histogram example
data = np.random.randn(1000)
mpt.hist(data, bins=20, color='green', edgecolor='black')
mpt.title("Histogram Example")
mpt.show()