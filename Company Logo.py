#!/bin/python3
import collections
import math
import os
import random
import re
import sys



""" if __name__ == '__main__':
    s = input()
 """
s=input()
s=sorted(s)
Fre=collections.Counter(s)
for k,v in Fre.most_common(3):
    print(k,v) 
 
#another way
s = sorted(input().strip())
    
    # finiding frequency 
s_counter =collections.Counter(s).most_common()
    
    # using lambda function sort the items with frequencies in deceding order
s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))

    # printing the first three items
for i in range(0, 3):
        print(s_counter[i][0], s_counter[i][1])    