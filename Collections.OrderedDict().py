from collections import OrderedDict

N=int(input())
d=OrderedDict()
for i in range(N):

    name,space,price=input().rpartition(' ')
    d[name]=d.get(name,0)+int(price)
    for name ,price in d.items():
        print(name,price)
