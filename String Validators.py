if __name__ == '__main__':
    a = input()

    print(any(s.isalnum() for s in a) )
    print(any(s.isalpha() for s in a) )
    print(any(s.isdigit() for s in a) )
    print(any(s.islower() for s in a) )
    print(any(s.isupper() for s in a) )
    
    
    
    
    
    
