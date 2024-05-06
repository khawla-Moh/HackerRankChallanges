""" a=int(input())
b=int(input())
c=int(input())
d=int(input())
 """
a,b,c,d=(int(input()) for _ in range(4))
print((a**b)+(c**d))
#print(pow(a,b)+pow(c,d))
