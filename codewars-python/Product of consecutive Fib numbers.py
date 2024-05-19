
def product_fib(_prod):
    a,b=0,1
    for i in range(_prod):
        if _prod > a*b:
            a,b = b , a+b
    return (a,b,_prod == a*b)      

print(product_fib(714))