""" n,m=map(int,input().split())

N_row=[input() for _ in range(n)]

k=int(input())

for r in sorted(N_row ,key=lambda r:int(r.split()[k])):
    print(r)
 """

s=[['1','2','3'],['5','3','2'],['9','8','7']]
