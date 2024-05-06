"""
import email.utils
import re

pattern=r'^[A-z].*\@[A-z]+\.[A-z]{1,3}$'
for _ in range(int(input())):
    format_email=email.utils.parseaddr(input())
    if re.match(pattern,format_email[0]):
        print(email.utils.formataddr(format_email)) 
    
 """
    #Another sloution
import re

for i in range(int(input())): 
    s = input()
    a = re.search(r'<[a-zA-Z][\w\.-]*@[a-zA-Z]*\.[a-zA-Z]{1,3}>', s)
    if bool(a):
        print(s)
    
