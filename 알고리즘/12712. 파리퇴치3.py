
T = int(input())

for tc in range(1,1+T):
    N,M = map(int,input().split())

    dr=[1,-1,0,0,1,1,-1,-1] #오른쪽 왼쪽 아래 위 오른쪽아래 왼쪽아래 왼쪽위 오른쪽위
    dc=[0,0,1,-1,1,-1,-1,1]

    lst= [list(map(int,input().split())) for _ in range(N)]

    maxn=0
    for x in range(N):
        for y in range(N):
            result = lst[x][y]
            for i in range(4):
                for j in range(1,M):
                    a = x+dr[i]*j
                    b = y+dc[i]*j
                    if 0<=a<N and 0<=b<N:
                        result += lst[a][b]
            if maxn < result:
                maxn=result
                #print(result)

            result1 = lst[x][y]
            for i in range(4,8):
                for j in range(1,M):
                    c = x+dr[i]*j
                    d = y+dc[i]*j
                    if 0<=c<N and 0<=d<N:
                        result1 += lst[c][d]
            if maxn < result1:
                maxn=result1
    print(f'#{tc} {maxn}')
