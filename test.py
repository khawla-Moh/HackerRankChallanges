def debug(func):
    def wrapper(a,b):
        print(f"Calling {func.__name__} with args: {a}, \
        kwargs: {b}")
        result = func(a, b)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper

@debug
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  













""" 
#decorator_function

def decorator_function(fun):

    def wrapper_fun():
        print("before calling")
        fun()
        print("after calling")
    return wrapper_fun

@decorator_function
def h():
     print('hello')

h()
 """














""" 
#secure data using closure
def secure_data(data):
    password = 'secret'
    
    def get_data(passw):
        if passw==password:
            return data
        else:
            return None
    return get_data
closure=secure_data('gogo')
print(closure('secret'))    
print(closure('none'))    
 """









""" 
def outer_function(x):
    def inner_function(y):
        return  y,x
    return inner_function

closure=outer_function(3)
print(closure(2))

 """





""" 
def outer(some_func):
     def inner():
         print ("before some_func")
         ret = some_func() # 1
         return ret + 1
     return inner
     def foo():
        return 1
     decorated = outer(foo) # 2
     decorated()
 """
""" 
def outer(fun):
    def inner():
        print("this is inner")
        rest=fun()
        return rest +1
    return inner

def foo():
    return 1

decoreator=outer(foo)
decoreator()
 """
                     




""" 

def add (x,y):
    return x+y
def sub(x,y):
    return x-y


def apply(fun,x,y):
    return fun(x,y)

print(apply(add,3,4))
print(apply(sub,3,4))
 """




""" def outter():
    x=1
    
    def inner():
        print(x)
    inner()


outter()
""" 
"""#x="global string"
def fo(a,b=0):
    return a-b
    
print(fo(1))
print(fo(4,3))
print(fo())

 """