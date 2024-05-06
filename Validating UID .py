# Enter your code here. Read input from STDIN. Print output to 
import re
testCase=input()
for i in range(int(testCase)):
    case=input().strip()
    if case.isalnum() and len(case)==10:
        if bool(re.search(r'^*[A-Z]){,2}',case)) and bool(re.search(r'(.*[0-9]{3,}',case)):
            if re.search(r'.*(.).*\1+.*',case):
                print ('Invalid')
            else:
                print ('Valid')    
        else:
            print ('Invalid')
    else:
        print ('Invalid')



""" 
A valid UID must follow the rules below:

It must contain at least 

uppercase English alphabet characters.
It must contain at least
digits ( -
).
It should only contain alphanumeric characters (
- , - & -
).
No character should repeat.
There must be exactly

    characters in a valid UID.

Input Format
 """