# Enter your code here. Read input from STDIN. Print output to STDOUT

input_m=int(input())
M=set(map(int,input().split()))
input_n=int(input())
N=set(map(int,input().split()))
a=(M.difference(N))
b=(N.difference(M))
U=a.union(b)

for i in sorted(U):
    print(i)
