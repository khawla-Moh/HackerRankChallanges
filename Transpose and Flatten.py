import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())


"""
 import numpy
n,m=map(int,input().split())

s = numpy.array([map(int, input().split()) for _ in range(n)])
print(numpy.transpose(s))
print(s.flatten())




 """

"""
 We can generate the transposition of an array using the tool numpy.transpose.
It will not affect the original array, but it will create a new array 
"""