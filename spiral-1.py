#  File: spiral.py
#  Description:
#  Student Name: Arun Mahadevan Sathia Narayanan
#  Student UT EID: as235872
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 50184
#  Date Created: 09/12/2024
#  Date Last Modified:

import math
import sys

#THIS IS JUST A HELPER METHOD NO NEED TO DEBUG
def create_blank_grid(length, width):
    """HELPER METHOD"""
    grid = []
    for i in range(length):
        grid.append([])
        for _ in range(width):
            grid[i].append(0)

    return grid

#THIS IS JUST A HELPER METHOD NO NEED TO DEBUG
def print_grid(grid):
    """HELPER METHOD"""
    printed_grid = create_blank_grid(len(grid), len(grid[0]))

    max_length = [-1] * len(grid)
    length_grid0 = len(grid[0])
    length_grid = len(grid)
    for j in range(length_grid0):
        for i in range(length_grid):
            printed_grid[i][j] = str(grid[i][j]) + " "
            if len(printed_grid[i][j]) > max_length[j]:
                max_length[j] = len(printed_grid[i][j])

    len_printed_grid = len(printed_grid)
    len_printed_grid0 = len(printed_grid[0])
    for i in range(len_printed_grid):
        row = ""
        for j in range(len_printed_grid0):
            row += (printed_grid[i][j] + " " * (max_length[j] - len(printed_grid[i][j]) + 1))
        print(row)


def find_fib_number(one_prev, two_prev, multiplicity):
    """Finds the Fibonacci number"""
    limit = 100
    fib_number = one_prev + two_prev

    if fib_number > limit:
        fib_number = multiplicity
        fib_number *= -1
    return fib_number

def check_valid_space(row, col, grid):
    """Checks the valid space"""  
    length = len(grid)
    if row < 0 or row > length or col < 0 or col > length:
        return False
    return grid[row][col] == 0

def create_spiral(dim):
    """Create Spiral"""
    # create variable to store our spiral numbers
    grid = create_blank_grid(dim, dim)

    directions = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]

    cur_row = 0
    cur_col = 0
    two_prev = 0
    one_prev = 1
    cur_dir = 0


    for _ in range(dim ** 2):
        multiplicity = 1
        attempted_row = cur_row + directions[cur_dir][0]
        attempted_col = cur_col + directions[cur_dir][1]

        if check_valid_space(attempted_row, attempted_col, grid):
            cur_row = attempted_row
            cur_col = attempted_col
        else:
            cur_dir =  cur_dir + 1
            cur_row += directions[cur_dir][0]
            cur_col += directions[cur_dir][1]
            grid[cur_row][cur_col] = find_fib_number(one_prev, two_prev, multiplicity)

        if grid[cur_row][cur_col] >= one_prev:
            two_prev = one_prev
            one_prev = grid[cur_row][cur_col]
        elif grid[cur_row][cur_col] == 0:
            break
        else:
            #we are flipping back the signal we set earlier to correct it
            grid[cur_row][cur_col] *= -1
            multiplicity += 1
            one_prev = 0
            two_prev = multiplicity

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
                base_row = i
                base_col = j

    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row = i
            new_col = j
            if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                total += grid[new_row][new_col]

    return total

def main():
    """Main function"""
    while True:
        try:
            input1 = input()
            if input1 != "":
                dim = int(input1)
                grid = create_spiral(dim)
            input2 = input()
            if input2 != "":
                sum_val = int(input2)

            adj_sum = sum_sub_grid(grid, sum_val)

            print(adj_sum)
        except ValueError:
            continue

main()
