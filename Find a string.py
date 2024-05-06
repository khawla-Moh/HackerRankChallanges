def count_substring(string, sub_string):
    count=0
    while sub_string in string:
        c=string.find(sub_string)
        string=string[c+1:]
        count +=1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    
    print(count_substring(string, sub_string))

    '''
    def count_substring(string, sub_string):
    return sum(string[i:].startswith(sub_string) for i in range(len(string)))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    '''