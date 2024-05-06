import re
s=input()
sub=input()
pattern=re.compile(sub)
match=pattern.search(s)
if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(s, match.start() + 1)