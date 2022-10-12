<<<<<<< HEAD:알고리즘/1979. 어디에 단어가 들어갈 수 있을까.py
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
=======
>>>>>>> fe69eb07c808e9ba1d3f1b5aac24cf7945af391f:박현영/1979. 어디에 단어가 들어갈 수 있을까.py

T = int(input())

for tc in range(1,1+T):
    N, K = map(int,input().split())
<<<<<<< HEAD:알고리즘/1979. 어디에 단어가 들어갈 수 있을까.py
    #print (K)
    lst=[input().split() for _ in  range(N)]
    #print(lst)
=======

    lst=[input().split() for _ in  range(N)]
>>>>>>> fe69eb07c808e9ba1d3f1b5aac24cf7945af391f:박현영/1979. 어디에 단어가 들어갈 수 있을까.py
    cnt1=0
    for x in range(N):
        cnt=0
        for y in range(N): #3
<<<<<<< HEAD:알고리즘/1979. 어디에 단어가 들어갈 수 있을까.py
            while cnt == K:
                if lst[x][y] == "1":
                    cnt+=1
                elif lst[x][y] == "0":
                    cnt=0
=======
            if lst[x][y] == "1":
                cnt+=1 #끝까지 돌고
            elif lst[x][y] == "0":
                if cnt == K:
                    cnt1+=1
                cnt = 0
        if cnt == K:
            cnt1 += 1
>>>>>>> fe69eb07c808e9ba1d3f1b5aac24cf7945af391f:박현영/1979. 어디에 단어가 들어갈 수 있을까.py


        cnt=0
        for y in range(N):
            if lst[y][x] == "1":
                cnt+=1
<<<<<<< HEAD:알고리즘/1979. 어디에 단어가 들어갈 수 있을까.py
                if cnt == K:
                    cnt1 += 1
                    continue
            elif lst[y][x] == "0":
                cnt=0


    print(cnt1)
=======
            elif lst[y][x] == "0":
                if cnt==K:
                    cnt1+=1
                cnt = 0
        if cnt == K:
            cnt1 += 1


    print(f'#{tc} {cnt1}')
>>>>>>> fe69eb07c808e9ba1d3f1b5aac24cf7945af391f:박현영/1979. 어디에 단어가 들어갈 수 있을까.py
