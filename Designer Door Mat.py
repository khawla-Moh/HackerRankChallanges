# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M=map(int,input().split())

for i in range(N//2):
    j=int((2*i)+1)
    print(('.|.'*j).center(M, '-'))
print('WELCOME'.center(M,'-'))
for i in reversed(range(N//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(M, '-'))
