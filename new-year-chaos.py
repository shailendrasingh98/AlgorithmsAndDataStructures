#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    s = 0

    for i in range(1, len(q)+1):
        p = q[i-1]
        if p - i>2:
            print('Too chaotic')
        for j in range(max(p-2,0), i-1):
            if q[j] > p:
                s+=1
    print(s)

if __name__ == '__main__':
    '''t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))'''
        #[1 2 5 3 7 8 6 4]
    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
