T = int(input())

for tc in range(1, 1+T):
    n= int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]


    empty=[]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                if (arr[i-1][j]==0 or i-1<0) and (arr[i][j-1]==0 or j-1<0):
                    empty.append([i,j])

    bin = []
    for m in range(len(empty)): #0 1 2
        x=empty[m][0] #00 = 2
        y=empty[m][1] #01 =0
        cnt1 =0
        cnt2=0
        for l in range(n):
            if x+l<n:
                if arr[x+l][y]!=0:
                    cnt1+=1
                else:
                    break
        for l in range(n):
            if y+l<n:
                if arr[x][y+l] !=0:
                    cnt2+=1
                else:
                    break

        bin.append([cnt1,cnt2])


    for a in range(len(bin)-1):
        for b in range(a+1,len(bin)):
            if bin[a][0]*bin[a][1]>bin[b][0]*bin[b][1]:
                bin[a],bin[b]=bin[b],bin[a]
            elif bin[a][0]*bin[a][1]==bin[b][0]*bin[b][1]:
                if bin[a][0] > bin[b][0]:
                    bin[a],bin[b] =bin[b],bin[a]

    print(f'#{tc} {len(bin)}',end= " ")


    for f in bin:
        for g in f:
            print(g,end=" ")

    print()



