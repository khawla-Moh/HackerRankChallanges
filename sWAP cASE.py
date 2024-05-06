def swap_case(s):
    result=[]
    for char in s:
        if char.islower():
            result.append(char.upper())
        else:
            result.append(char.lower())
    return ''.join(result)



    """ result=""

    for i in s:
        if s.isupper==True:
            result+=i.lower()
        elif s.isupper()==False :
            result+=i.upper()

    return result      
     """    
    

    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)