#  File: spiral.py
#  Description:
#  Student Name: Arun Mahadevan Sathia Narayanan
#  Student UT EID: as235872
#  Partner Name: Pranav Belligundu
#  Partner UT EID: psb898
#  Course Name: CS 313E
#  Unique Number: 50184
#  Date Created: 09/12/2024
#  Date Last Modified:

# import math
import sys

#THIS IS JUST A HELPER METHOD NO NEED TO DEBUG
def create_blank_grid(length, width):
    grid = []
    for i in range(length):
        grid.append([])
        for j in range(width):
            grid[i].append(0)
    
    return grid

#THIS IS JUST A HELPER METHOD NO NEED TO DEBUG
def print_grid(grid):
    printed_grid = create_blank_grid(len(grid), len(grid[0]))
    
    maxLength = [-1] * len(grid);

    for j in range (len(grid[0])):
        for i in range (len(grid)):
            printed_grid[i][j] = (str(grid[i][j]) + " ")
            if len(printed_grid[i][j]) > maxLength[j]:
                maxLength[j] = len(printed_grid[i][j])
         
    for i in range (len(printed_grid)):
        row = ""
        for j in range (len(printed_grid[0])): 
            row += (printed_grid[i][j] + " " * (maxLength[j] - len(printed_grid[i][j]) + 1))
        print(row)


def find_fib_number(onePrev, twoPrev, multiplicity):
    """Finds the Fibonacci number"""
    LIMIT = 100
    fib_number = onePrev + twoPrev

    if fib_number > LIMIT:
        fib_number = multiplicity
        return fib_number * -1
    return fib_number

def check_valid_space(row, col, grid):
    """Checks the valid space"""  
    length = len(grid)
    #if row < 0 or row > length or col < 0 or col > length: old code
    if row < 0 or row >= length or col < 0 or col >= length:
        return False
    return grid[row][col] == 0

def create_spiral(dim):
    # create variable to store our spiral numbers
    grid = create_blank_grid(dim, dim)

    directions = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]        
    
    curRow = 0
    curCol = 0


    twoPrev = 0
    onePrev = 1

    curDir = 0


    for i in range(dim ** 2):
        multiplicity = 1
        attemptedRow = curRow + directions[curDir][0]
        attemptedCol = curCol + directions[curDir][1]

        if check_valid_space(attemptedRow, attemptedCol, grid):
            curRow = attemptedRow
            curCol = attemptedCol
        else:
            curDir =  curDir + 1
            curRow += directions[curDir][0]
            curCol += directions[curDir][1]
            grid[curRow][curCol] = find_fib_number(onePrev, twoPrev, multiplicity)

        if grid[curRow][curCol] >= onePrev:
            twoPrev = onePrev
            onePrev = grid[curRow][curCol]
        elif grid[curRow][curCol] == 0:
            break
        else:
            #we are flipping back the signal we set earlier to correct it
            grid[curRow][curCol] *= -1
            multiplicity += 1
            onePrev = 0
            twoPrev = multiplicity
        
    print_grid(grid)

    return grid

def sum_sub_grid(grid, val):
    """Sums the sub grid"""
    base_row = -2
    base_col = -2
    len_grid = len(grid)
    len_grid0 = len(grid[0])
    for i in range(len_grid):
        for j in range(len_grid0):
            if grid[i][j] == 0:
                return -1
            elif grid[i][j] == val:
                i = base_row
                j = base_col

    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row = i
            new_col = j
            if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                total += grid[new_row][new_col]

    return total


def main():
    """main with input through terminal"""
    while True:
        try: #try catch block for invalid input
            input1 = input()
            if input1 == "":
                break
            dim = int(input1)
            grid = create_spiral(dim)

            input2 = input()
            if input2 == "":
                break
            sum_val = int(input2)

            adj_sum = sum_sub_grid(grid, sum_val)
            print(adj_sum)

        except ValueError:
            #if invalid input
            print("String Invalid Input")
            continue

"""
def main():
    #takes input from the spiral-1.in input file
    input_stream = sys.stdin
    lines = input_stream.read().strip().split()

    current_line = 0

    while current_line < len(lines):
        try:
            dim = int(lines[current_line])
            current_line += 1

            #fib spiral
            grid = create_spiral(dim)
            print_grid(grid)

            if lines[current_line].isdigit():
                sum_val = int(lines[current_line])
                current_line += 1

                #sum of 3x3 subgrid around the found value
                adj_sum = sum_sub_grid(grid, sum_val)
                print(adj_sum)

        except ValueError:
            #if the input is not a number
            print('String Invalid Input')
            current_line += 1
"""
main()
