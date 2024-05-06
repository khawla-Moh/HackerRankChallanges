def print_formatted(number):
    binNum=format(number,'b')
    size=len(binNum)    
    for i in range(1,number+1):
        octNum=format(i,'o')
        hexNum=format(i,'X')
        binaNum=format(i,'b')
        print(str(i).rjust(size),str(octNum).rjust(size),str(hexNum).rjust(size),str(binaNum).rjust(size))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)