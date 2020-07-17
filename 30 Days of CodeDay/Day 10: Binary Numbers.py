#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    current_cnt = 0
    max_cnt = 0
    while(n > 0) :
        temp = n %2
        if temp == 1:
            current_cnt += 1
            if(current_cnt > max_cnt) :
                max_cnt = current_cnt
        else:
            current_cnt = 0
        n = n//2

    print(max_cnt)
