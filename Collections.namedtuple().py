""" # Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
name_student=input()
total_marks=0
for _ in range(n):
    students = namedtuple('my_student', name_student)
    MARKS, CLASS, NAME, ID = input().split()
    my_student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(my_student.MARKS)
print((total_marks / n)) """
x=10
y=5
print(f"{x}-{y}")
x=x-y
y=y+y
print(f"{x}-{y}")