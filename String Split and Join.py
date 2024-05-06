def split_and_join(line):
    # write your code here
    l=line.split()
    return '-'.join(l)

if __name__ == '__main__':
    s=input()
    print(split_and_join(s)) 
