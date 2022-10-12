# SWEA 2805. 농작물 수확하기

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    M = N // 2
    ans = 0
    for i in range(N):
        if i <= M:
            for j in range(M - i, M + i + 1):
                ans += arr[i][j]
        else:
            for j in range(i - M, N - (i - M)):
                ans += arr[i][j]


    print(f"#{tc} {ans}")