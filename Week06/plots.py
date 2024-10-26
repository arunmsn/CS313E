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

def plot(domain):
    """plots the functions given a domain max value"""
    x = np.linspace(0, domain)
    plt.plot(x, f1(x), label = "f1", color = 'red')
    plt.plot(x, f2(x), label = "f2", color = 'blue')
    plt.plot(x, f3(x), label = "f3", color = 'green')
    plt.legend()
    plt.show()

plot(5)
plot(15)
plot(50)
