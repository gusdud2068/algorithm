import sys

sys.stdin = open("sample_input (3).txt", "r")

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split()) #가로세로 길이 N 회문 길이 M
    lst = [list(input()) for _ in range(N)]
    #print(lst)

    v=""
    for x in range(N):
        for y in range(N-M+1): #시작점
            c = []
            for z in range(M):#8글자
                c+=lst[x][y+z]
            if c==c[::-1]:
                for d in c:
                    v+=d
            c=[]
            for z in range(M):
                c+=lst[y+z][x]
            if c==c[::-1]:
                for d in c:
                    v+=d
    print(v)
