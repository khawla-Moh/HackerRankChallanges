cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    a,b,c=0,1,1
    for _ in range(n):
        yield a
        a, b = b, a + b
     
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


""" cube = lambda x:x*x*x # complete the lambda function 

def fibonacci(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, [fibonacci(i) for i in range (n)]))) 
 """