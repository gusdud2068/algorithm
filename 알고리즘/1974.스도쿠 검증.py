
T= int(input())

for tc in range(1,T+1):
    lst=[list(map(int,input().split())) for _ in range(9)]

    result = 1

    for i in range(9):
        arr=[0]*10 #빈칸
        for j in range(9):
            arr[lst[i][j]]+=1
            if arr[lst[i][j]] != 1:
                result =0
                break

    for i in range(9):
        arr=[0]*10
        for j in range(9):
            arr[lst[j][i]]+=1
            if arr[lst[j][i]] != 1:
                result =0
                break

    for l in range(0, 9, 3):
        for h in range(0,9,3): #0 3 6
            arr = [0] * 10
            for i in range(l,l+3):
                for j in range(h,h+3):
                    arr[lst[i][j]]+=1
                    if arr[lst[i][j]] != 1:
                        result = 0
                        break

    print(result)