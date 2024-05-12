import string


def caesarCipher(s, k):
    encrypted = ''
    for char in s:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) -base  + k)%26 +base )
        else:
            encrypted += char
    return encrypted


print(caesarCipher('middle-Outz',3))

""" 
s2=[]
pattren=['-','_','.',"'",',']
pattrenz=['Z','z']
def caesarCipher(s, k):
    k1=25
    for i in s:
        if i in pattren:
            s2.append(i)
        elif i in pattrenz:
            s2.append(chr(ord(i)-k1))
             
        else:
            s2.append(chr((ord(i) + k) ))
    return ''.join(s2) 
 

print(caesarCipher('middle-Outz',3)) #Nkdzod-daA """