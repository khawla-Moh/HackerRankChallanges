""" import re
s=input()
m=re.search(r'([a-z0-9])\1+',s)
if m is None:
    print(-1) 
else:
    print (m.group(0)[1])
 """
import re
S=input()
n=re.search(r'([a-zA-Z0-9])\1+',S)

if n is None:
    print('-1')
else:
    print(n.group(0)[1])        
