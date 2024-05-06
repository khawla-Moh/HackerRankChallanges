if __name__ == '__main__':
    arr=[]
    sorces_arr=[]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        sorces_arr.append(score)

    sorces_arr.sort()
    s_min=0
    mini=sorces_arr[0]
    arr.sort()
    for i in sorces_arr:
        if i !=mini:
            s_min=i
            break
    for i in arr:
        if i[1]==s_min:
            print(i[0])


    