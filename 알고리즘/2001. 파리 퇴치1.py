t= int(input())

for tc in range(1,1+t):

    n,m = map(int,input().split())

    arr=[list(map(int,input().split())) for _ in range(n)]

    max1=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum1=0
            for x in range(m):
                for y in range(m):
                    sum1+=arr[i+x][j+y]

            if max1<sum1:
                max1=sum1
    print(f'#{tc} {max1}')