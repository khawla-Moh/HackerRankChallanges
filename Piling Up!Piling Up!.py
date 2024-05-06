from collections import deque
for _ in range (int(input())):
    _,que=input(),deque(map(int,input().split()))
    for c in reversed(sorted(que)):
        if que[-1] == c:que.pop()
        elif que[0]== c:que.popleft()
        else:
            print('No')
            break
    else:
        print('Yes')






















""" 
t = int(input())
for i in range(t):
    size = int(input())
    top = 2**31
    d = deque(list(map(int,input().split())))
    for j in range(len(d)):
        if d[0]>=d[len(d)-1] and d[0]<=top:
            top = d.popleft()
        elif d[len(d)-1]<=top:
            top = d.pop()
        else:
            print('No')
            break
    if len(d) == 0:
        print('Yes')
         """