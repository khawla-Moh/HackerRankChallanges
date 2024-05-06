
if __name__ == '__main__':
    l=[]
    N = int(input())
    for _ in range(N):
        command=list(input().split())
        if command[0].lower()=='insert':
            l.insert(int(command[1]),int(command[2]))
            
        if command[0].lower()=='remove':
            l.remove(int(command[1]))
 
        if command[0].lower()=='append':
            l.append(int(command[1]))
 
        if command[0].lower()=='sort':
            l.sort()
        if command[0].lower()=='pop':
            l.pop()
        if command[0].lower()=='reverse':
            l.reverse()
        if command[0].lower()=='print':
            print(l)
     
 
  





""" insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse """