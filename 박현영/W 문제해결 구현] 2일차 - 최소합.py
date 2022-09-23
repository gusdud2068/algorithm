def dfs(i,j,sums):
    global mins

    if i<n and j<n:
        sums += arr[i][j]
        dfs(i+1,j,sums)
        dfs(i,j+1,sums)

        if i==n-1 and j==n-1:
            if mins>sums:
                mins=sums
    return


T = int(input())
for tc in range(1,1+T):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]

    mins=((n-1)+(n-2))*10

    dfs(0,0,0)

    print(f'#{tc} {mins}')