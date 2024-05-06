from itertools import combinations
N_integers=int(input())
list_letters=input().split()
K_selected=int(input())
combinations_letters =list (combinations(list_letters,K_selected))
pos=len([i for i in combinations_letters if 'a' in i ])


print(pos/len(combinations_letters))

