def get_middle(s):
    middle_letter=len(s)//2
    for i in range(len(s)):
        if len(s)%2 ==0:
            return "" + s[middle_letter -1 : middle_letter +1]
        else:
           return s[middle_letter]

    

print(get_middle('testse'))    