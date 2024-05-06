def merge_the_tools(string, k):
    merg = []
    len_merge=0
    for i in string:
        len_merge +=1
        if i not in merg:
            merg.append(i)
        if len_merge == k:
            print(''.join(merg))
            merg=[]
            len_merge=0
                        
                        
                        


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)