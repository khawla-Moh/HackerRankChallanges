for _ in range(int(input())):
    a=int(input())
    A=set(input().split())
   
    b=int(input())
    B=set(input().split())
    if (A.issubset(B)):
        print('True')
    else:
        print('False')
    
    
 