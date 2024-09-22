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
