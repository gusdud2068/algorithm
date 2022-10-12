def dfs(x, sums):
    global mins

    for i in range(N):
        if visited[i] == 0:
            sums += arr[x][i]
            visited[i] = 1
            dfs(i, sums)
            sums -= arr[x][i]
            visited[i] = 0

    if sum(visited) == N:
        sums += arr[x][0]
        if sums < mins:
            mins = sums
        return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [1] + [0] * (N - 1)
    mins = 1000

    dfs(0, 0)

    print(f'#{tc} {mins}')