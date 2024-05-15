def move_zeros(lst):
    ls=[]
    for i in lst:
      if i ==0:
         lst.remove(i)
         lst.append(i)
        
    return lst

print(move_zeros([1,2,3,0,3,2,0,2]))