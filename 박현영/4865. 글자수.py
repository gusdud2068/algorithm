T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    maxn=0
    for i in str1:
        cnt=0
        for f in str2:
            if i == f:
                cnt+=1
                if maxn < cnt:
                    maxn = cnt

    print(f'#{tc} {maxn}')

