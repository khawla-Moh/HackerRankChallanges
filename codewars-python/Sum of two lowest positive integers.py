import math
def sum_two_smallest_numbers(numbers):
    #your code here
    arr=[]
    arr.append(min(numbers))
    numbers.remove(min(numbers))
    print(arr,numbers)
    s=numbers
    print(s)
    print(numbers)
    arr.append(min(s)) 
    return int(sum(arr))


print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))