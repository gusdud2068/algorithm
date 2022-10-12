T = int(input())
# n= 4
for tc in range(1,1+T):
    n=int(input())

    arr=[[0]*n for _ in range(n)]

    dc = [1,0,-1,0]
    dr = [0,-1,0,1]#아왼위오
    cnt=1
    for i in range(1): # 012
        for j in range(n):#012
            arr[i][j]=cnt
            cnt+=1

    # if i == 0 and j == 0:
    #     print(f'#{tc}')
    #     print(1)
    #     continue

    mi,mj = -1,-1
    turn =0
    for k in range(n-1,-1,-1): # 3 2 1 0
        for l in range(k): #0 1 2
            mi=i+dc[turn]*(l+1)
            mj=j+dr[turn]*(l+1)

            arr[mi][mj]=cnt
            cnt+=1
        i,j = mi, mj

        turn =(turn+1)%4 #1

        for l in range(k):  # 0 1 2
            mi = i + dc[turn] * (l + 1)
            mj = j + dr[turn] * (l + 1)

            arr[mi][mj] = cnt
            cnt += 1
        i, j = mi, mj

        turn = (turn + 1) % 4
    print(f'#{tc}')
    for l in arr:
        print(*l)

