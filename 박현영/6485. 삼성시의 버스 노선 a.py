T = int(input())

for tc in range(1,1+T):
    N= int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())

    arr1 = [int(input()) for _ in range(P)]
    lst = [0]*5001

    for k in range(N): # 0 1
        for i in range(arr[k][0],(arr[k][1])+1):
            lst[i]=lst[i]+1

    print(f'#{tc}',end=' ')

    for l in arr1:
        print(lst[l], end=" ")
    print()