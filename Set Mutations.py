a=int(input())
A=set(map(int,input().split()))
for _ in range(int(input())):
    command=input().split()
    set_b=set(map(int,input().split()))

    eval('A.{}({})'.format(command[0],set_b))
    print(sum( A))           

    #Python eval()
    '''
    Python eval() function is used to parse an expression as an argument and then execute it within the Python program.
    The Python eval() is a built-in function that allows us to evaluate the Python expression as a ‘string’ and return the value as an integer
                        
    eval(expression, globals = None, locals = None)

                
    '''