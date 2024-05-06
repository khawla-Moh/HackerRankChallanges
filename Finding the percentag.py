if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    """ if query_name ==name:
        result=sum(student_marks[name])/len(student_marks[name]) 
        print(format(result,'.2f'))
 """
    chosing_input=student_marks[query_name]
    result=sum(chosing_input)/len(chosing_input) 
    print(format(result,'.2f'))

