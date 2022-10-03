# T = int(input())
#
# for tc in range(1,1+T):
#     N, K = map(int,input().split())
#     #print (K)
#     lst=[list(map(int,input().split())) for _ in  range(N)]
#
#     cnt1=0
#     for x in range(N):
#         for y in range(N-K+1): #3
#             cnt = 0
#             for i in range(K): #0.1.2
#                 if lst[x][y+i] == 1:
#                     cnt+=1
#             if cnt == K:
#                 cnt1+=1
#     #cnt2=0
#     for x in range(N-K+1):
#         for y in range(N):
#             cnt = 0
#             for i in range(K):
#                 if lst[y][x+i]==1:
#                     cnt+=1
#             if cnt == K:
#                 cnt1+=1
#
#     print(cnt1)

    #  for y in range(N):
    #         if lst[y][x]==1:
    #             cnta+=1
    #             if lst[y][x] ==0:
    #                 continue
    #     if cnta == K:
    #         cnt1 +=1
    # print(cnt1)

T = int(input())

for tc in range(1,1+T):
    N, K = map(int,input().split())
    #print (K)
    lst=[input().split() for _ in  range(N)]
    #print(lst)
    cnt1=0
    for x in range(N):
        cnt=0
        for y in range(N): #3
            while cnt == K:
                if lst[x][y] == "1":
                    cnt+=1
                elif lst[x][y] == "0":
                    cnt=0


        cnt=0
        for y in range(N):
            if lst[y][x] == "1":
                cnt+=1
                if cnt == K:
                    cnt1 += 1
                    continue
            elif lst[y][x] == "0":
                cnt=0


    print(cnt1)