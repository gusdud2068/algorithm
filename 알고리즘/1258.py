

T = int(input())

for tc in range(1,1+T):
    n=int(input())
    lst=[list(map(int,input().split())) for _ in range(n)]

    print(lst)

    empty=[]
    sum2=0
    for i in range(n):
        sum1 = 0
        for j in range(n):
            if lst[i][j]!=0:
                sum1+=1
        if lst[i][j] != 0:
            sum2 += 1
    empty.append(sum1)
    empty.append(sum2)


    print(empty)


