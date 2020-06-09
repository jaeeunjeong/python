#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 0 : 
        result = 1
    else :
        recursion = factorial(n-1)
        result = n*recursion
    
    return result




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)   

    fptr.write(str(result) + '\n')

    fptr.close()
