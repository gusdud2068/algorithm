
T = int(input())

for tc in range(1,1+T):
    N=int(input()) #수열의 길이
    M=list(map(int,input()))

    maxn=0
    cnt=0
    for i in range(N):
        if M[i] ==1:
            cnt+=1
        else:
            cnt = 0
        if maxn<cnt:
            maxn=cnt

    print(maxn)