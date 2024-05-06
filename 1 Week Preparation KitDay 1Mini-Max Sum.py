#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    lenArr=len(arr)
    minimum=0
    maximum=0
    for i in range(lenArr,len(arr)-1):
        minimum=sum(arr[i])
    for j in range(lenArr):
        maximum=sum(arr[j])
        
    return minimum ,maximum       
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
