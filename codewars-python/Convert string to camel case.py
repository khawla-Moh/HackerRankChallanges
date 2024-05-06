import re




def to_camel_case(text):    
     arr1 = [n for n in text]
     if len(arr1) != 0: 
      for i in range(len(arr1)):
       if arr1[i] in ('-', '_'):
        arr1[i+1] = arr1[i+1].upper()
     arr1 = ''.join([i for i in arr1 if i not in ('-', '_')])
     return arr1    

    
    
    
    


def to_camel_case(text):    
     
    return text[0]+text.title()[1:].replace('-','').replace('_','') 
    
"""
    ssequence[start:end:step]
    arr=[]
    for i in text:
       if text[i] in pattern:
           text[i]=text[i].
           arr.append()
    return a
 """


print(to_camel_case('fkerjkefjwejjf-fek_jfeowij_l-oro_jk'))
