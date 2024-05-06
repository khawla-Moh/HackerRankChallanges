import re
def fun(s):
    pattern=re.compile('^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$')
    return pattern.match(s)

def filter_email(email):
     return list[filter(fun,email)]

n=int(input())
email=[]
for _ in range (n):
     email.append(input())

f_email=filter_email(email)
f_email.sort()
print(f_email)





""" def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails) """