
import sys
sys.stdin = open("input (2).txt","r")


for tc in range(1,11):
    T = int(input())
    lst=[list(input()) for _ in range(100)]
    #print(lst)

    maxlen =0

    for x in range(100):
        for y in range(100):
            c=[]
            for z in range(100-y):
                c+=lst[x][y+z]
                if c==c[::-1]:
                    if len(c)>maxlen:
                        maxlen=len(c)


            c=[]
            for z in range(100-y):
                c+=lst[y+z][x]
                if c == c[::-1]:
                    if len(c) > maxlen:
                        maxlen = len(c)

    print(f'#{tc} {maxlen}')
