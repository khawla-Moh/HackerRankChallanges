import numpy
l=map(int,input().split())
m=[]
for i in range(l[0]):
    m.append(map(int,input().split()))
m=numpy.array(m)
print(max(numpy.min(m,axis=1)))

""" 
import numpy

n,m=map(int,input().split())

lista=[list(map(int,input().split())) for i in range(n)]

ar=numpy.array(lista)

print(max(numpy.min(ar,axis=1)))
 """