T = int(input())
for tc in range(1,1+T):
    N,M = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(M)]
    board=[[0]*(N+1) for _ in range(N+1)]
    dr = [1,-1,0,0,1,1,-1,-1]
    dc = [0,0,-1,1,1,-1,-1,1]
    board[int(N / 2+1)][int(N / 2)+1] = 2
    board[int(N / 2)][int(N / 2)] =2
    board[int(N / 2 +1)][int(N / 2)] = 1
    board[int(N / 2)][int(N / 2) +1] = 1

    print(lst)
    for i in range(M):
        x=lst[i][0]
        y=lst[i][1]

        board[x][y]=lst[i][2] # 돌 놓기

        for j in range(8):
            nx=x
            ny=y


    print(board)


