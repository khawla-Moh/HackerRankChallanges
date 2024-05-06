import numpy

""" 
fd,sd,td=map(int,input().split(" "))


print( numpy.zeros((fd,sd,td),dtype=numpy.integer))    
print( numpy.ones((fd,sd,td),dtype=numpy.integer))     """
N = tuple(map(int, input().split()))
print(numpy.zeros(N, int))
print(numpy.ones(N, int))