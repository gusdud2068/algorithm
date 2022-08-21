import sys

sys.stdin = open("input (6).txt", "r")
T = 10

for tc in range(1, T + 1):
    t = input()
    lst = [list(input()) for _ in range(100)]

    max1 = 0
    for x in range(101):
        c = ''
        for i in range(2, 101):
            for y in range(100 - i-1):
                for j in range(i):
                    c+=lst[x][y+j-1]
                    if c == c[::-1]:
                        if max1 < len(c):
                            max1 = len(c)
                    else:
                        c=lst[x][j + 1:101]

    for x in range(101):
        c = ''
        for i in range(2, 101):
            for y in range(100-i-1):
                for j in range(i):
                    c+=lst[y][x+j-1]
                    if c == c[::-1]:
                        if max1 < len(c):
                            max1 = len(c)
            else:
                c+=(lst[x][j + 1:101])

    print(max1)
