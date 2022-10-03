T = 10

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for tc in range(1, 1 + T):
    N = int(input())
    lst = [list(input()) for _ in range(16)]

    ans = 0
    x, y = 0, 0

    for i in range(16):
        for j in range(16):
            if lst[i][j] == "2":
                x, y = i, j

    stack = [(x, y)]
    while stack:  # 스택이 빌때까지
        px, py = stack.pop()
        for a in range(4):
            ni = px + dr[a]
            nj = py + dc[a]
            if 0 <= ni < 16 and 0 <= nj < 16:
                if lst[ni][nj] == "0":
                    stack.append((ni, nj))
                    lst[ni][nj] = "1"
                elif lst[ni][nj] == "3":
                    ans = 1
                    stack.clear()
                    break

    print(f'#{N} {ans}')
