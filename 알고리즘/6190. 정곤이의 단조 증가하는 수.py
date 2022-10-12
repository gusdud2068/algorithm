T = int(input())
for tc in range(1,1+T):

    n=int(input())
    arr=list(map(int,input().split()))


    max1=-1
    for i in range(0,n-1): #0,3
        for j in range(i+1,n):
            sum1=arr[i]*arr[j]
            a=list(str(sum1))

            for l in range(len(a)-1):
                if int(a[l])> int(a[l+1]):
                    break
            else:
                if sum1>max1:
                    max1=sum1

    print(f'#{tc} {max1}')