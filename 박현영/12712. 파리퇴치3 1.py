t= int(input())

for tc in range(1,1+t):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]

    dc = [1,-1,0,0,1,-1,1,-1]
    dr = [0,0,1,-1,1,-1,-1,1]

    max1=0
    for i in range(n):
        for j in range(n):

            sum1 = arr[i][j]
            for l in range(4):
                for k in range(1,m+1):
                    mi=i+dc[l]*k
                    mj=j+dr[l]*k

                    if 0<=mi<n and 0<=mj<n:
                        sum1+=arr[mi][mj]
            if sum1 >= max1:
                max1 = sum1

            sum1 = arr[i][j]
            for h in range(4,8):
                for q in range(1,m+1):
                    mi = i + dc[h] * q
                    mj = j + dr[h] * q

                    if 0 <= mi < n and 0 <= mj < n:
                        sum1 += arr[mi][mj]
            if sum1 >= max1:
                max1 = sum1


    print(max1)