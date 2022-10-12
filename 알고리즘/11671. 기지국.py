t = int(input())

for tc in range(1,1+t):
    n = int(input())
    arr= [list(input()) for _ in range(n)]

    dc=[0,0,1,-1]
    dr=[1,-1,0,0]

    for a in range(n):
        for b in range(n):
            for c in range(4):
                if arr[a][b] == 'A':
                    x=a+dc[c]
                    y=b+dr[c]
                    if 0 <= x < n and 0 <= y < n:
                        if arr[x][y] == "H":
                            arr[x][y] = "X"
                elif arr[a][b] == 'B':
                    for d in range(1,3):
                        x = a + dc[c]*d
                        y = b + dr[c]*d
                        if 0<=x<n and 0<=y<n:
                            if arr[x][y] == "H":
                                arr[x][y] = "X"

                elif arr[a][b] == 'C':
                    for d in range(1,4):
                        x = a + dc[c]*d
                        y = b + dr[c]*d
                        if 0 <= x < n and 0 <= y < n:
                            if arr[x][y] == "H":
                              arr[x][y] = "X"

    cnt=0
    for f in range(n):
        for e in range(n):
            if arr[f][e] =="H":
                cnt+=1

    print(cnt)

