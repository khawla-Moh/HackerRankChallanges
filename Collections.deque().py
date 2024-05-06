from collections import deque
d=deque()
for _ in range(int(input())):
    command=input().split()
    if command[0]=='append':
        d.append(int(command[1]))
    elif command[0]=='appendleft':
        d.appendleft(int(command[1]))
    elif command[0]=='popleft':
        d.popleft()
    else :
        d.pop()

for i in d:
    print(i, end = ' ')        
""" for i in range(len(d)):
    print(d.popleft(), end = ' ')    """