"""plots.py"""

import matplotlib.pyplot as plt
import numpy as np

# TASK 1
# Regular Plots
def f1(n):
    """first function"""
    return n**10 + 10.1**n + 2**n

def f2(n):
    """second function"""
    return 2**n + n**100 + 8

def f3(n):
    """third function"""
    return 2**(2**n) + n**2

def f4(n):
    """third function"""
    return 25.5**n + n**100 + n**50

def plot(domain):
    """plots the functions given a domain max value"""
    x = np.linspace(0, domain)
    plt.plot(x, f1(x), label = "f", color = 'red')
    plt.plot(x, f2(x), label = "g", color = 'blue')
    plt.plot(x, f3(x), label = "h", color = 'green')
    #plt.plot(x, f4(x), label = "j", color = 'orange')
    plt.legend()
    plt.show()

plot(1.1)

"""
                        6
                    28      39
                7   8       3   27
            5   1   2   4
            
                    28
            7               8
        5       1       2       4

                    39
                3       27

"""