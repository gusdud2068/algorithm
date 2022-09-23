jinsoo={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
        'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

T=int(input())
for tc in range(1,T+1):
    N,data=input().split() #4 47FE

    num=[]
    for i in data:
        num.append(jinsoo[i])

    f = ""
    for j in range(len(num)): #num[j]
        a=num[j]
        b=["0"]*4
        c=[]
        d=3
        while a != 0:
            b[d] = str(a % 2)
            a=a//2
            d-=1
        for e in b:
            f+=e

    print(f'#{tc} {f}')
