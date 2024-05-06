import numpy
N,M=map(int,input().split())

matrix=numpy.array([input().split() for _ in range(N)],int )

print(numpy.mean(matrix,axis=1))
print(numpy.var(matrix,axis=0))
print(numpy.std(matrix))