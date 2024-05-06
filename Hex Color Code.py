# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern=r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})'
for _ in range(int(input())):
    string0=input()
    m=re.findall(pattern,string0)
    if m:
        print(*m,sep='\n')


