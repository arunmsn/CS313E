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

def check_valid_space(row, col, grid):
    """Checks the valid space"""  
    length = len(grid)
    if row < 0 or row > length or col < 0 or col > length:
        return False
    return True

def find_fib_number(two_prev, one_prev):
    """Finds the next Fibonacci number"""
    return two_prev + one_prev

def create_spiral(dim):
    """Create Spiral"""
    grid = create_blank_grid(dim, dim)
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # right, down, left, up
    cur_row = 0
    cur_col = 0
    two_prev = 1
    one_prev = 1  # Start with 1, 1
    cur_dir = 0
    reset_start = 2  # The number to start with after reset

    for i in range(dim ** 2):
        if i == 0 or i == 1:
            fib_number = 1  # First two numbers are 1
        else:
            fib_number = find_fib_number(two_prev, one_prev)

        if fib_number > 100:
            fib_number = reset_start
            two_prev = 0
            one_prev = reset_start  # Reset sequence
            reset_start += 1  # Increment reset start for next time
        else:
            two_prev, one_prev = one_prev, fib_number  # Continue Fibonacci sequence

        grid[cur_row][cur_col] = fib_number

        # Find next valid position
        for _ in range(4):  # Try all directions
            attempted_row = cur_row + directions[cur_dir][0]
            attempted_col = cur_col + directions[cur_dir][1]
            if (0 <= attempted_row < dim and
                0 <= attempted_col < dim and
                grid[attempted_row][attempted_col] == 0):
                cur_row = attempted_row
                cur_col = attempted_col
                break
            cur_dir = (cur_dir + 1) % 4  # Change direction if current is invalid
        else:  # If we've tried all directions and found no valid move
            break

    print_grid(grid)
    return grid

def sum_sub_grid(grid, val):
    """Sums the 3x3 sub grid centered on the given value"""
    dim = len(grid)

    # Find the position of the given value
    center_row = -1
    center_col = -1
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] == val:
                center_row = i
                center_col = j
                break
        if center_row != -1:
            break

    # If the value is not found, return -1
    if center_row == -1:
        return -1

    total = 0
    for i in range(center_row - 1, center_row + 2):
        for j in range(center_col - 1, center_col + 2):
            if 0 <= i < dim and 0 <= j < dim:
                total += grid[i][j]

    return total

def main():
    """ main method """
    while True:
        try:
            dim = int(input())
            if dim < 20:
                grid = create_spiral(dim)
                sum_val = int(input())
                adj_sum = sum_sub_grid(grid, sum_val)
                print(adj_sum)
            else:
                print(-1)
                sum_val = int(input())
                print(-1)
        except ValueError:
            print("String Invalid Input")
            continue
        except EOFError:
            break

main()
