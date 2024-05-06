import numpy
N,M,P=map(int(input().split()))
n=numpy.array([map(int, input().split()) for _ in range(N)])
m=numpy.array(map(int,input().split()))
print(numpy.concatenate(n,m))