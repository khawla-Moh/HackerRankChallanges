import re 


for _ in range(int(input())):
    str1 = input()
    str1= re.sub(r"(?<= )(&&)(?= )", "and", str1)
    print(re.sub(r"(?<= )(\|\|)(?= )", "or", str1))



