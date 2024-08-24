import re
def simplify(poly):
    
    
    matches = re.findall(r'([+\-]?)(\d*)([a-z]+)', poly)
    expand=[[int(i[0] + (i[1] if i[1] != "" else '1')),''.join(sorted(i[2]))] for i in matches ]
    variable=sorted(list(set(i[1] for i in expand)),key=lambda x:(len(x),x))
    ceo={n:sum(i[0] for i in expand if i[1]==n) for n in variable}

    return '+'.join(str(ceo[v]) + v for v in variable if ceo[v] != 0).replace('1','').replace('+-','-')


print(simplify('x+y-2xy+yx'))








