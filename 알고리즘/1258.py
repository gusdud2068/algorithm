T = int(input())

for tc in range(1, 1+T):
    n= int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

<<<<<<< HEAD
    #print(lst)

    empty=[]


    for i in range(n):
        for j in range(n):
            if lst[i-1][j] ==  0   and lst[]




    print(lst)


=======

    empty=[]
    for i in range(n):
        for j in range(n):
            if (arr[i-1][j]==0 or i-1<0) and (arr[i][j-1]==0 or j-1<0):
                empty.append([i,j])
>>>>>>> 54a811128dac37db3e0ee4487683dc5b3a392cb4



