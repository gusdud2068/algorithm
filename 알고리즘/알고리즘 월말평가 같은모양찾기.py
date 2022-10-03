T=int(input())
for t in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    arr1=[list(map(int,input().split())) for _ in range(3)]
    ho=0
    for i in range(n-2):
        for j in range(n-2):
            count=0
            for y in range(3):
                for x in range(3):
                    if arr[i+y][j+x]==arr1[y][x]:
                        count+=1
                    else:
                        break
                if arr[i + y][j + x] != arr1[y][x]:
                    break
            if count==9:
                ho+=1
    print(ho)