#Replace With Alphabet Position

def to_camel_case(text):
        cap=False
        newText=''
        for i in text:
                if i =='-' or i=='_':
                        cap=True
                
                        continue
                else:
                    if cap==True:
                           i=i.upper()
                    newText = newText + i
                    cap = False
        return newText
        
        

      


print(to_camel_case('nfjkjfj-e_h-io'))