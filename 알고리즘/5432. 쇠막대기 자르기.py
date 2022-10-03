T = int(input())

for tc in range(1,1+T):
    N = input()
    build = 0
    cnt = 0
    for i in range(len(N)):
        if N[i] == '(':
            build += 1
        elif N[i] == ')':
            build -= 1
            if N[i-1] == '(':
                cnt += build
            else:
                cnt += 1
    print(f'#{tc} {cnt}')