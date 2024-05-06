
if __name__ == '__main__':

    n = int(input())

    Tuple1 = map(int, input().split())

    t = tuple(Tuple1)

    print(hash(t));
""" 
    
if __name__=='__main__':
    n =int(input())

    s=input().split()
    data=list(map(int,s))
    
    
    print(hash(tuple(data))) """