from itertools import combinations    
S,k =input().split()
for i in range(1,int(k)+1):
    for j in combinations(sorted(S),i):
        print(''.join(j))
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,k =input().split()
for i in range(1, int(k)+1):
    for j in combinations(sorted(s), i):
        print (''.join(j))

     
'''