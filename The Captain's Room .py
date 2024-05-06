group_size=int(input())

counts=dict()
room_number=input().split()
for i in room_number:
    if i not in counts:
        counts[i]=1
    else:
        counts[i]+=1
for i in counts:
        if counts[i]==1:
            print(i)








    








""" counts = dict()
n = input()
number = input().split()
for i in number:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1
for i in counts:
    if counts[i] == 1:
        print (i)




gruop_size=int(input())
d={}
for i in input().split():
    d[i]=d.get(i,0)+1

for key in d:
    if d[key] != gruop_size:
        print(i)
        break
 """
""" group_size=input()
room_number=set(input())
l=[]
for i in room_number:
    if l==group_size:
        room_number.
        
        

print(l) """