import math
import os
import random
import re
import sys

def runningMedian(a):
    sorted_a = sorted(a)
    medians = []
    for i in range(len(sorted_a)):
        total = 0
        count = 0
        for j in range(i+1):
            total += sorted_a[j]
            count += 1
        medians.append(total/count)
    for val in medians[0:len(medians)-1]:
        print(val)

runningMedian([10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
