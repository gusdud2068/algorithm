T = int(input())

for tc in range(1,T+1):
    N, Q = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(Q)]

    lst=[0]*(N+1)

    for j in range(1,Q+1):
        for i in range(arr[j-1][0],arr[j-1][1]+1):
            lst[i]=j

    print(f"#{tc}", end=" ")

    for i in range(1,len(lst)):
        print(lst[i], end=" ")
    print()