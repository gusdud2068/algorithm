
T = int(input())

for tc in range(1,1+T):
    n,m,k = map(int,input().split())
    arr = list(map(int,input().split()))
    ans="Possible"

    arr.sort() #4,3

    arr1=[0]*(1+arr[-1])

    for i in range(0,len(arr1),m):
        arr1[i]=k
        arr1[0]=0

    sum1 = 0
    for j in arr:
        for k in range(0,j+1):
            sum1+=arr1[k]
        sum1-=1
        arr1[k] -= 1

        if sum1<0:
            ans="Impossible"

    print(f'#{tc} {ans}')