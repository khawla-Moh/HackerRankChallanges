import re

for _ in range(int(input())):
    try:
        string=input()
        a=(re.compile(string))
        print(bool(a))
    except re.error:
        print('False')
            

                
        

