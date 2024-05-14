def divisors(integer):
    arr=[]
    for i in range(2,integer):
        if integer % i==0:
            arr.append(i)
        
          
    return arr if len(arr) > 0 else "{} is prime".format(integer)
                
 

print(divisors(13))