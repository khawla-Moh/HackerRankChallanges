def solution(text, ending):
    # your code here...
    #return text.endswith(ending)
    if len(text) < len(ending):
        return False
    for (x,y) in zip(text[::-1],ending[::-1]):
        if x == y:
            return True
        return False


print(solution('abc','bc'))


