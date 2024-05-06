n=int(input())
words=[input() for i in range(n)]

word_ocuurance={}
for i in words:
    word_ocuurance[i]=0
for i in words:
    word_ocuurance[i] +=1    
print(len(word_ocuurance))
p= word_ocuurance.values()
for i in p:
    print(i, end=" ")