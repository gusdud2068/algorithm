
T = int(input())

for tc in range(1,1+T):
    N, M = list(map(int,input().split()))
    lst=[list(map(int,input().split())) for _ in range(N)]

    dr=[1,-1,0,0,1,-1,-1,1]
    dc=[0,0,1,-1,1,-1,1,-1]


    maxn=0
    for x in range(N):
        for y in range(N):
            plus=lst[x][y]
            for i in range(4):
                for j in range(1,M):
                    a=x+dr[i]*j
                    b=y+dc[i]*j

                    if 0<=a<N and 0<=b<N:
                        plus+=lst[a][b]

            if plus>maxn:
                maxn=plus

            plus=lst[x][y]
            for l in range(4,8):
                for h in range(1,M):
                    c=x+dr[l]*h
                    d=y+dc[l]*h
                    if 0<=c<N and 0<=d<N:
                        plus+=lst[c][d]
            if plus>maxn:
                maxn=plus

    print(f'#{tc} {maxn}')




