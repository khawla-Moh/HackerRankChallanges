from itertools import permutations

a,b=input().split()

for i in sorted(permutations(a,int(b))):
    print(''.join(i))