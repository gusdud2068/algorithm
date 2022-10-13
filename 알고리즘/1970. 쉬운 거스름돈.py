T = int(input())

for tc in range(1,1+T):
    arr=int(input())
    money=[50000,10000,5000,1000,500,100,50,10]
    check=[0]*len(money)
    for i in range(len(money)):
        if arr>=money[i]:
            check[i]=arr//money[i]
            arr=arr%money[i]
    print(f'#{tc}')
    print(*check)