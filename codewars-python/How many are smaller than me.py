def smaller(arr):
    # Good Luck!
    arr2=[]
    for index in range (len(arr)):
        count=0
        for small_number in range(index +1 ,len(arr)):
            if arr[index] > arr[small_number]:
                count +=1
        arr2.append(count)
        
               
    #print(count)              
    return arr2    

def smaller(arr):
    # Good Luck!
    return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]

def smaller(arr):
    return [sum(b < a for b in arr[i + 1:]) for i, a in enumerate(arr)]

def smaller(arr):
    return [sum(x > y for y in arr[i+1:]) for i, x in enumerate(arr)

r=[4, 3, 2, 1, 0]        
print(smaller(r))        







"""    for num in arr:
        arr2=[]
        count_length=[]                    
        counting=0
    
        for smaller_num in arr:
                if smaller_num < num:
                     counting +=1
                     #print(counting)
                     count_length.append(counting)
                     #print(count_length)
                     r=len(count_length)
                     #print(r)
                     arr2.append(r)
                     #print(arr2)
        print(arr2) 
  """          
