from collections import defaultdict
n,m =map(int,input().split())

d=defaultdict(list)

for i in range(n):
    A=input()
    d[A].append(i+1)
for j in range(n):
    B=input()
    if B in d:
        print(*d[B])
    else:
        print(-1)
    
