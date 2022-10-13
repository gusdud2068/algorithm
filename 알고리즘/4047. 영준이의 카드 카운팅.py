

T = int(input())

for tc in range(1,1+T):
    arr=list(str(input()))
    S=[0]*14
    D = [0] * 14
    H = [0] * 14
    C = [0] * 14
    result=0
    #result=[]
    for i in range(0,len(arr),3):
        if arr[i]=='S':
            if S[int(arr[i+1]+arr[i+2])]==1:
                result=1
                break
            S[int(arr[i + 1] + arr[i + 2])] = 1


        elif arr[i]=='D':

            if D[int(arr[i+1]+arr[i+2])]==1:
                result=1
                break
            D[int(arr[i + 1] + arr[i + 2])] = 1


        elif arr[i]=='H':

            if H[int(arr[i+1]+arr[i+2])]==1:
                result=1
                break
            H[int(arr[i + 1] + arr[i + 2])] = 1


        elif arr[i]=='C':

            if C[int(arr[i+1]+arr[i+2])]==1:
                result=1
                break
            C[int(arr[i + 1] + arr[i + 2])] = 1
    if result==1:
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc} {13-S.count(1)} {13-D.count(1)} {13-H.count(1)} {13-C.count(1)}')



