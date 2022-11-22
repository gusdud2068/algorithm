T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    empty = []
    for i in range(N):      # 왼쪽 위  끝부분 인덱스 모아서 A에 담기
        for j in range(N):
            if arr[i][j] != 0:  # 좌표 (i, j)가 0이 아니라면
                if (arr[i - 1][j] == 0 or i - 1 < 0) and (arr[i][j - 1] == 0 or j - 1 < 0):   # 왼쪽이랑 위가 0이거나 범위 밖이라면
                    empty.append((i, j))

    B = []      # 행, 열 , 곱을 담을 리스트
    for x in range(len(empty)):  # 0 1 2
        m = empty[x][0]  # 00 = 2
        n = empty[x][1]  # 01 =0

        garo = 0
        sero = 0
        while 1:
            if arr[m][n] != 0:  # 0이 아니라면 세로 한칸씩 증가
                sero += 1
            else:       # 0 이라면,
                m -= 1   # 0으로 갔던거 다시 뒤로 돌아가기
                break
            m += 1

        while 1:
            if arr[m][n] != 0:
                garo += 1
            else:
                n -= 1
                break
            n += 1

        B.append([sero, garo, sero * garo])  #
    print(B)

    for q in range(len(B) - 1):    # 선택정렬, 내자신과 내이후의 것들 비교하기
        for w in range(q + 1, len(B)):
            if B[q][2] > B[w][2]:  # 행렬 크기로 비교 (1순위)
                B[q], B[w] = B[w], B[q]
            elif B[q][2] == B[w][2] and B[q][0] > B[w][0]: # 행렬크기가 같다면, 행크기로 비교 (2순위)
                B[q], B[w] = B[w], B[q]

    print(f'#{tc} {len(B)}', end=' ')
    for C in B:  # B를 돌아서 ( 행, 열 ) 순으로 출력
        print(C[0],C[1], end=' ')

    print()