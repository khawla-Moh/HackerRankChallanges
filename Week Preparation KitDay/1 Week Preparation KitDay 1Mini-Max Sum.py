#!/bin/python3


















"""
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
    count=0
    
    for i in range(lenArr):
        count+=arr[i]
    minimum= count-max(arr) 
    maximum= count-min(arr) 
        

    print( minimum ,maximum )      
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    """