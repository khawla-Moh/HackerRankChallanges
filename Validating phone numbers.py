import re
pattern='[798]\d{9}$'   #$ asserts position at the end of a line
for _ in range(int(input())):
    #print(str(bool(re.match(pattern,input()))))
    if re.match(pattern,input()):
        print('YES')
    else:
        print('NO')

