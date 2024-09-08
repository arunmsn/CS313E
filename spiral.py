"""
  File: spiral.py
  Description: Create a table of values starting from 1 in a spiral pattern depending upon
               the number of rows and columns. Then, taking in the input for a specific
               value, output the sum of the numbers adjacent to that number.

  Student Name: Arun Mahadevan Sathia Narayanan
  Student UT EID: as235872

  Partner Name: Anirudh Anandula
  Partner UT EID: ara4275

  Course Name: CS 313E
  Unique Number: 50184 (Arun)
  Unique Number: 50183 (Ani)
  Date Created: 09/03/2024
  Date Last Modified: 09/03/2024

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n

def create_spiral(n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")

 Input: spiral is a 2-D list and n is an integer
 Output: returns an integer that is the sum of the
         numbers adjacent to n in the spiral
         if n is outside the range return 0

def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
"""

from itertools import count
from collections import namedtuple

def steps_from_center():
    """
    if dim is odd:
        move right one step
        move down N steps
        move left N steps
    else:
        move left one step
        move up N steps
        move right N steps
    """
    Step  = namedtuple("Step", ["dx", "dy"])
    right_step = Step( 1,  0)
    down_step  = Step( 0,  1)
    left_step  = Step(-1,  0)
    up_step    = Step( 0, -1)

    for n in count(start=1):
        if n % 2:
            yield right_step
            for _ in range(n):
                yield down_step
            for _ in range(n):
                yield left_step
        else:
            yield left_step
            for _ in range(n):
                yield up_step
            for _ in range(n):
                yield right_step

def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""
    if dim % 2 == 0:
        dim += 1
    grid = [[""] * dim for _ in range(dim)]

    # and we start by placing a 1 in the center:
    x = y = int(dim / 2)
    grid[y][x] = 1

    for i, step in enumerate(steps_from_center(), start=2):
        if i > dim**2:
            break
        x += step.dx
        y += step.dy
        grid[y][x] = i

    return grid

def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    n = len(grid)
    for r in range(n):
        for c in range(n):
            if grid[r][c] == val:
                total = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue  # Skip the center cell
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            total += grid[nr][nc]
                return total
    return 0  # Return 0 if val is not found in the grid

def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    #file = open('spiral.in', 'r')
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            to_read = input()
            if to_read != '':
                sum_val = int(to_read)
            else:
                break

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            return "End of File"

if __name__ == "__main__":
    main()
