#!/bin/python3

import sys

def findMedian(arr):
    m=len(arr)//2
    arr = sorted(arr)
    return arr[m]

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr)
    print(result)