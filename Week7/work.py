"""
    File: work.py
    Description:
        Input: the number of test cases (T), 
        		then T lines of input each with n lines of code and k factor 
        Output: The type of search and the time it took

    Student Name: Arun Mahadevan Sathia Narayanan
    Student UT EID: as235872

    Partner Name: N/A
    Partner UT EID: N/A

    Course Name: CS 313E
    Unique Number: 50184 (Arun)
    Date Created: 10/11/2024
    Date Last Modified: 10/11/2024
"""

import sys
import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v, k):
    """Returns the sum of the series given v lines of code and k productivity factor"""
    if k == 0:
        return 0
    if k == 1:
        return v
    total = v
    while v > 0:
        v //= k
        total += v
    return total

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    """linear search to return v, the min lines of code to write"""
    v = 1
    total = sum_series(v, k)
    while total < n:
        v += 1
    return v


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    """binary search to return v, the min lines of code to write"""
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if sum_series(mid, k) < n:
            left = mid + 1
        else:
            right = mid - 1
    return left


def main():
    """main function"""
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int (line)

    for _ in range (num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp =  line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

if __name__ == "__main__":
    main()
