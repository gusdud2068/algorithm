import sys

sys.stdin = open("input (2).txt", "r")

T = 10
for tc in range(1, 11):
    t = int(input())
    room = [list(input()) for _ in range(100)]

    maxword = 0

    for x in range(100):
        for y in range(100):
            c=""
            for z in range(100-y):
                c+=room[x][y+z]
                if c == c[::-1]:
                    if len(c)>maxword:
                        maxword=len(c)

    for x in range(100):
        for y in range(100):
            c=""
            for z in range(100-x):
                c+=room[x+z][y]
                if c==c[::-1]:
                    if len(c)>maxword:
                        maxword=len(c)

    print(f'#{tc} {maxword}')