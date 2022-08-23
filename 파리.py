T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split()) for _ in range(N))]


def ret(i,j):
    sum = 0
    for y in range(M):
        a=y+i
        for x in range(M):
            b=x+j
            sum += arr[a][b]
    return sum

Max = 0
for i in range(N-M+1):
    for j in range(N-M+1):
        ret = arr[i][j]
        if ret > Max:
            Max = ret

print(f'#{tc} {ret}')