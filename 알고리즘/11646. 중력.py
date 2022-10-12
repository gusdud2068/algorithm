t =int(input())
for tc in range(1,1+t):
    n=int(input())
    lst=list(map(int,input().split()))

    max1 = 0
    for l in lst:
        if max1<l:
            max1=l

    arr = [[0]*n for _ in range(max1)]

    for i in range(n):
        k = lst[i]
        for j in range(k):
            arr[j][i]=1
    maxi=0

    for i in range(max1):
        for j in range(n-1):
            if arr[i][j] == 1:
                cnt=0
                for k in range(j+1,n):
                    if arr[i][k]==0:
                        cnt+=1
                if maxi<cnt:
                    maxi=cnt
    print(maxi)



