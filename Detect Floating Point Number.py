import re

pattern =re.compile( '[+-]?[0-9]*\.[0-9]+')
def floatin_reg(s):
    if pattern.fullmatch(s):
        return True
        
    else:
        return False




s=int(input())
for i in range(s):
    str_reg=input()
    print(floatin_reg(str_reg))
     
     