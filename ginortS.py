s='Soring1234'
s=sorted(s)
""" lower_case =sorted([i for i in S if i.islower()])
upper_case =sorted([i for i in S if i.isupper()])
digit_case =sorted([i for i in S if i.isdigit()])
sorted_string="".join(lower_case+upper_case+digit_case) """
sorted_string= [i for i in s if i.islower()]+\
[i for i in s if i.isupper()]+\
[i for i in s if i.isdigit() and int(i)%2 != 0 ] +\
[i for i in s if i.isdigit() and int(i)%2 == 0 ]

print(''.join(sorted_string))