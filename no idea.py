""" # Enter your code here. Read input from STDIN. Print output to STDOUT
import ast
n,m=input().split(" ")

arr=input().split()

A=set(input().split())
B=set(input().split())

initial_happinest=0


print(sum([(i in A)-(i in B) for i in arr])   ) """
initial_happinest=0

n,m=input().split(' ')
arr=([int(i) for i in input().split(' ')])

A=set([int(i) for i in input().split(' ')])
B=set([int(i) for i in input().split(' ')])
for i in arr:
    if i in A:
        initial_happinest +=1
    if i in B:
        initial_happinest -=1
print(initial_happinest)