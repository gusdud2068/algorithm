T = int(input())
for tc in range(1, T+1):

    code = ["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]
    N, M = map(int,input().split()) #세로 가로

    arr=[input() for _ in range(N)]

    k=[]
    for i in range(N):
        for j in range(M-1,-1,-1):
            if arr[i][j] == "1":
                b=j
                c=i
                for a in range(b,b-56,-1):
                    k.append(arr[c][a])
                break
        if len(k)>0:
            break


    arr1=[]
    for m in range(56-1,-1,-7):
        s=''
        for n in range(7):
            number=k[m-n]
            s+=number
        arr1.append(s)


    arr2=[]
    for e in range(8):
        for d in range(10) :
            if code[d] == arr1[e]:
                arr2.append(d)

    odd = 0
    even = 0
    for f in range(0,8,2):
        odd += arr2[f]
    for g in range(1, 8, 2):
        even += arr2[g]

    answer = (odd*3)+even

    if answer%10>0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(arr2)}')

