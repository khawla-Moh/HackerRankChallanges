#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
     
     format1= '%a %d %b %Y %H:%M:%S %z'
     t1=datetime.strptime(t1,format1)
     t2=datetime.strptime(t2,format1)
     return str(int(abs(t1-t2).total_seconds()))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

'''
The format string you provided, '%a %d %b %Y %H:%M:%S %z', is a common format used in Python's datetime module to represent a datetime object as a formatted string. Let's break down the format string:

    %a represents the abbreviated weekday name (e.g., "Mon", "Tue", etc.).
    %d represents the zero-padded day of the mo

    nth (e.g., "01", "02", etc.).
    %b represents the abbreviated month name (e.g., "Jan", "Feb", etc.).
    %Y represents the four-digit year (e.g., "2021", "2022", etc.).
    %H represents the zero-padded hour in 24-hour format (e.g., "00", "01", etc.).
    %M represents the zero-padded minute (e.g., "00", "01", etc.).
    %S represents the zero-padded second (e.g., "00", "01", etc.).
    %z represents the UTC offset in the format "+HHMM" or "-HHMM" (e.g., "+0530", "-0800", etc.).

To format a datetime object according to this format string, you can use the strftime() method. Here's an example:
python
'''
   