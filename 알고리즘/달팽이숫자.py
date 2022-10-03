t=int(input())

for tc in range(1,1+t):
    n=int(input())

    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    arr=[[0]*n for _ in range(n)]

    cnt=1
    i=0
    j=0
    d=0
    arr[i][j]=cnt

    while n*n>cnt:
        ni=i+dc[d]
        nj=j+dr[d]
        if 0<=ni<n and 0<=nj<n and arr[ni][nj]==0:
            cnt+=1
            arr[ni][nj]=cnt

            i=ni
            j=nj

        else:
            d+=1
            d=d%4


