T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T + 1):

    N = int(input())
    arr = [[0] * N for _ in range(N)]  # 0,1,2 안에 각각 0*3번

    # 초기값
    i, j, cnt, d = 0, 0, 1, 0  # cnt=처음 자리 d는 방향
    arr[i][j] = cnt
    cnt = cnt + 1

    while cnt <= N * N:
        ni = i + di[d]  # next i가 f리스트 di의 d번째만큼 움직이는것
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:  # 만큼 가면 종료
            i, j = ni, nj
            arr[i][j] = cnt  # 움직일 자리
            cnt = cnt + 1
        else:
            d = (d + 1) % 4  # di 리스트 가 4개가 있기때문

    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()