#!/bin/python3

import math
import os
import random
import re
import sys

def findSortedPosition(data, lst):
    # Start with the entire sequence of elements.
    low = 0
    high = len(lst)-1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        # Find the midpoint of the sequence.
        mid = (low+high)//2
        # Does the midpoint contain the target?
        if lst[mid] == data:
        # Index of the target
            return mid
        # Or does the target precede the midpoint?
        elif data < lst[mid]:
            low = mid+1

        else:
        # Or does it follow the midpoint?

            high = mid-1

    # Index where the target value should be.
    return low

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    #score = set(scores)
    sc = unique(scores)
    l = []
    for a in alice:
        ind = findSortedPosition(a, sc)+1
        l.append(ind)
    return l

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #scores_count = int(input())

    scores = [100, 90, 90, 80 ,75 ,60]#list(map(int, input().rstrip().split()))

    #alice_count = int(input())

    alice = [50, 65, 77, 90, 102]#list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print(result)
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
