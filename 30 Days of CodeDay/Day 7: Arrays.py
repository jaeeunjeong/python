#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    result = ''
    #print(arr)
    #for i in reversed(arr):
    #print(i)
    #print(arr[::-1])
    for i in arr : 
        result = result + str(i) + " "
    print(result)
