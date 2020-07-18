#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    s = 0
    max_sum = -100
    for i in range(4) :
        for j in range(4) :
            s = arr[i][j+0]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j+0]+arr[i+2][j+1]+arr[i+2][j+2]
            max_sum = max(s,max_sum)

    print(max_sum)
