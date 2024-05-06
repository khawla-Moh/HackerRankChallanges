
for _ in range(int(input())):

    


    try:
        a,b=map(int,input().split())
        print (int(a/b))
    except Exception as e:
           print ("Error Code:" ,e)
















""" Errors detected during execution are called exceptions.

Examples:

ZeroDivisionError

ValueError
This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value. 
 """