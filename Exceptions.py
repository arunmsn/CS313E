"""Catching Exceptions"""
def is_float(val):
    """Verifies if an input can be converted to be a float, and handles exceptions"""
    try:
        print(float(val))
        return True
    except ValueError as v:
        print(val, v)
        return False
    finally:
        print('all inputs are processed')
        
def zero_div(val):
    try:
        out = int(val) / 0
    except ZeroDivisionError as d:
        print(d)

my_list = input().split()
for value in my_list:
    zero_div(value)
    is_float(value)
