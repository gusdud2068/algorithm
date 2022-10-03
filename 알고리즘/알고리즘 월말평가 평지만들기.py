t = int(input())

for tc in range(1,1+t):
    n=int(input())
    x,y,i,j = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]


    sum1=0
    for m in range(x,i+1):
        for n in range(y,j+1):
            sum1+=arr[m][n]


    avr1 = sum1 // (((i - x) + 1) * ((j - y) + 1))


    sum2=0
    for m in range(x,i+1):
        for n in range(y,j+1):
            if avr1>=arr[m][n]:
                sum2+=avr1-arr[m][n]
            else:
                sum2+=arr[m][n]-avr1

    print(f'#{tc} {sum2}')

