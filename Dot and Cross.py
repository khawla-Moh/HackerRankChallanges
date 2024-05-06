import numpy as np
n=int(input())
a = np.array([input().split() for _ in range(n)],dtype=int)
b = np.array([input().split() for _ in range(n)],dtype=int)

matrix0=[]
for i in range(n):
    r=[np.dot(a[i,:],b[:,m]) for m in range(n) ]
    matrix0.append(r)
matrix0=np.array(matrix0)
print(matrix0)
