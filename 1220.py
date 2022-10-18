T = int(input())

for tc in range(1, 1+T):
    n= int(input())
    arr = list(map(int,input().split()))
    max1=0
    for i in arr:
        if max1<i:
            max1=i

    arr1 = [[0]*n for _ in range(max1)]

    for l in range(n):
        for m in range(arr[l]):
            arr1[m][l]=1

    print(arr1)
    max2=0
    for k in range(max1):
        cnt=0
        for j in range(n):
            if arr1[k][j] ==0:
                cnt+=1
        if max2<cnt:
            max2=cnt

    print(max2)
