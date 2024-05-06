# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
for k,c in groupby(input()):
    print ( "(%d, %d) "% (len(list(c)),int(k)),end='')


#another way using fun
def main(string):
    
    # using for loop to iterate through the string
    for k, c in groupby(string):
        
        #printing the output
        print("(%d, %d)" % (len(list(c)), int(k)), end=' ')
        
# calling the function
main(input())