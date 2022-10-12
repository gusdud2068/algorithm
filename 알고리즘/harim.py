T = int(input())
for tc in range(1,1+T):
    arr=list(map(int,input().split()))
    player1 =[0]*10
    player2=[0]*10
    ans=0

    for i in range(0,len(arr)):
        if i%2 == 1:

        player1[arr[i]]+=1
        j = i + 1
        player2[arr[j]] += 1
        if 3 in player1:
            ans=1
            break
        for l in range(0,8,3):
            if player1[l] == 1 and player1[l+1] == 1 and player1[l+2] == 1:
                ans=1
                break
        if ans==1:
            break
        if 3 in player2:
            ans=2
            break
        for k in range(0,8,3):
            if player2[k] == 1 and player2[k+1] == 1 and player2[k+2] == 1:
                ans=2
                break
        if ans==2:
            break

    print(f"#{tc} {ans}")
