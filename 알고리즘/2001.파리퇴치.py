import sys
sys.stdin = open("input (2).txt","r")

T = int(input())
for tc in range(1,1+T):
    N, M = map(int,input().split()) # 5 2
    lst=[list(map(int,input().split())) for _ in range(N)]
    #print(lst)

    maxn = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            c = 0
            for x in range(i+M):
                for y in range(j+M):
                    c+=lst[x][y]
            print(c)
            if maxn<c:
                maxn=c
    print(maxn)



