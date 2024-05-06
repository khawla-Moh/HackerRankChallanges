import numpy
N,M=map(int,input().split())

matrix=numpy.array([input().split() for _ in range(N)],int )

print(numpy.prod(numpy.sum(matrix,axis=0),axis=0))