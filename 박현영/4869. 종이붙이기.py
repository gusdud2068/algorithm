import sys
sys.stdin = open("input (2).txt", "r")

T =10
for tc in range(1,11):
    t=int(input())
    room=[list(input()) for _ in range(100)]

    maxword=0

    for x in range(100): #가로
        for y in range(99): #0부터 99까지 꺼내오기 시작점 세로
            c = ""
            for word in range(2,100-y): #회문의 길이
                for word1 in range(word):# 0 1 2 0 1 2 3
                    c += room[x][y+word1]
                    if c==c[::-1]:
                        if maxword<len(c):
                            maxword=len(c)
                    else:
                        y=y+1
                        if y>100:
                            break

    for x in range(100):
        for y in range(99):
            c=""
            for word in range(2,100-y):
                for word1 in range(word):
                    c += room[y][x+word1]
                    if c==c[::-1]:
                        if maxword<len(c):
                            maxword=len(c)
                    else:
                        x=x+1
                        if x>100:
                            break

    print(maxword)





