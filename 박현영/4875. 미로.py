
#이차배열
def dfs(i,j,N): #가로 세로

    stack=[]

    di=[-1,1,0,0] #행
    dj=[0,0,1,-1] #열


    while True:
        if arr[i][j] == 3:
            return 1 #갈수있으니깐 1
        arr[i][j] = 1 #현재위치 벽으로 바꿔줌

        for d in range(4): #델타 이동
            ni = di[d]+i #다음 갈 행
            nj = dj[d]+j

            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1:
                stack.append((i,j)) #두개 행과열 같이 저장 [현재위치]
                i,j = ni,nj #[이동]
                break
        else: #갈수있는 칸이 없으면
            if stack: #스택이 있다면 왔던길을 돌아가는것
                i,j =stack.pop() #다시 while로 돌아감
            else: # 스택이 비어있다면
                break #가장 가까운 반복문에서 나감 (끝을냄)

    return 0 #끝까지 돌았는데 길없으면 0


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    si = sj =0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si = i
                sj = j

    print(f"#{tc} {dfs(si, sj, n)}")