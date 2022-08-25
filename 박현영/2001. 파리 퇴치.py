
T = int(input())

for tc in range(1,T+1):
    N,M = list(map(int, input().split()))

    lst=[list(map(int,input().split())) for _ in range(N)]
    print(lst)
    maxa=0

    for i in range(N-M+1): #3까지
        for j in range(N-M+1): #3까지
            a=0
            for y in range(M):#0,1
                b=i+y
                for x in range(M):
                    c=j+x
                    a=a+lst[b][c]
                if maxa<a:
                    maxa=a
    print(maxa)

