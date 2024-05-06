def solution(s):
   if len(s) %2 !=0:
      s +='_'
   arr=[]
   for i in range(0,len(s),2):
      arr.append(s[i:i+2]) 
   return arr    
      
   
print(solution('abc'))


