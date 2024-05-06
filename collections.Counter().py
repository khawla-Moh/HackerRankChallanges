from collections import Counter

Nmber_shoes=int(input())
all_shoes_sizes=Counter(map(int,input().split()))
Nmber_customers=int(input())
t=0
for i in range(Nmber_customers):
    size,rate=map(int,input().split())
    if all_shoes_sizes[size]:
        all_shoes_sizes[size]-=1
        t+=rate
print(t)        
    
