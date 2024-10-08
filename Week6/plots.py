"""plots.py"""

import matplotlib.pyplot as plt
import numpy as np

# TASK 1
# Regular Plots
def f1(n):
    """first function"""
    return ((2 ** 10) *n) + (2 ** 10)

def f2(n):
    """second function"""
    return (n ** 3.5) - 1000

def f3(n):
    """third function"""
    return (100 * (n ** 2.1)) + 50


x = np.linspace(0, 5)
plt.plot(x, f1(x), label = "f1", color = 'red')
plt.show()

x = np.linspace(0, 15)
plt.plot(x, f2(x), label = "f1", color = 'blue')
plt.show()

x = np.linspace(0, 50)
plt.plot(x, f3(x), label = "f1", color = 'green')
plt.show()

# TASK 2
# Asymptotic Notation
