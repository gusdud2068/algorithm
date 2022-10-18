T = int(input())

for tc in range(1, 1+T):
    n= int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]


    empty=[]
    for i in range(n):
        for j in range(n):
            if (arr[i-1][j]==0 or i-1<0) and (arr[i][j-1]==0 or j-1<0):
                empty.append([i,j])

    print(empty)


