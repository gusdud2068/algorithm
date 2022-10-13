T = int(input())

for tc in range(1,1+T):
    n = int(input())

    arr = list(map(str,input().split()))

    a=[]

    for i in range((n//2)+(n%2)):
        a.append(arr[i])
        if i+(n//2)+(n%2)<n:
            a.append(arr[(i+n//2)+(n%2)])

    print(f'#{tc} {"".join(a)}')
