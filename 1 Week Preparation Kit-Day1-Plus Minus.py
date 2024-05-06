#els#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive=0
    negative=0
    zero=0
    l=len(arr)
    for i in range(l):
        if arr[i] <0:
            negative +=1
        elif arr[i]==0:
             zero +=1
        elif arr[i]>0 :
             positive+=1
             
            
    return print(positive/l , negative/l, zero/l,end='\n')             
  
                
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

 