
T = int(input())

for tc in range(1,1+T):
    N, K = map(int,input().split())

    lst=[input().split() for _ in  range(N)]
    cnt1=0
    for x in range(N):
        cnt=0
        for y in range(N): #3
            if lst[x][y] == "1":
                cnt+=1 #끝까지 돌고
            elif lst[x][y] == "0":
                if cnt == K:
                    cnt1+=1
                cnt = 0
        if cnt == K:
            cnt1 += 1


        cnt=0
        for y in range(N):
            if lst[y][x] == "1":
                cnt+=1
            elif lst[y][x] == "0":
                if cnt==K:
                    cnt1+=1
                cnt = 0
        if cnt == K:
            cnt1 += 1


    print(f'#{tc} {cnt1}')