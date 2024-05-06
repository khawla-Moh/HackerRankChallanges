
def wrapper(f):
    def fun(l):
        f(['+91 '+i[-10:-5]+' '+i[-5:] for i in l])
    return fun

@wrapper
def sort_phone(numbers):
    print(*sorted(numbers),sep='\n')

if __name__=='__main__':
    phone_number=[input() for _ in range(int(input())) ]
    sort_phone(phone_number)

'''
http://simeonfranklin.com/blo HackerRank/g/2012/jul/1/python-decorators-in-12-steps/
'''