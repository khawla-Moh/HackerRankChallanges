# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')




""" 

import numpy
n, m = map(int, input().strip().split())
A = []
B = []
for _ in range(n):
    A.append(map(int, input().strip().split()))
for _ in range(n):
    B.append(map(int, input().strip().split()))
    
numpy.array(A)
numpy.array(B)

print (numpy.add(A, B))
print (numpy.subtract(A, B))
print (numpy.multiply(A, B))
print (numpy.divide(A, B))
print (numpy.mod(A, B))
print (numpy.power(A, B)) """