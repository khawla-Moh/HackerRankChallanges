input()
s  = list(map(int, input().split()))
s.reverse()
s = set(s)
num_commands = int(input())
command = ["", ""]
for i in range(num_commands):
    command = input().split()
    if len(command) == 1:
        getattr(s, command[0])()
    elif len(command) == 2:
        command[1] = int(command[1])
        if command[1] in s:
            getattr(s, command[0])(command[1])
print(sum(s))












""" int_input=int(input())

a=set(map(int,input().split()))

input_command=int(input())
for i in range(input_command):
    command=input().split()
    if command[0]=="pop":
        a.pop()

    elif command[0]==' remove':
        a.remove(int(command[1]))
    elif command[0]==' discard':
        a.discard(int(command[1]))
    
print(sum(a))   
  """