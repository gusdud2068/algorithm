T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    start = 1
    end = N
    search = False

    while start <= end:
        middle = (start + end) // 2
        temp = middle ** 3

        if temp > N:
            end = middle - 1
        elif temp < N:
            start = middle + 1
        else:
            x = middle
            search = True
            break

    if search:
        print(f'#{tc} {x}')
    else:
        print(f'#{tc} -1')