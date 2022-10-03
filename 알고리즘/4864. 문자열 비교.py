T = int(input())
# XYPV
# EOGGXYPVSY

str1 = input()  # 4
str2 = input()  # 10

for tc in range(1, T + 1):
    cnt = 0

    for i in range(len(str2)):
        if str2[i: i + len(str1)] == str1:
            cnt += 1

    print(f'#{tc} {cnt}')
