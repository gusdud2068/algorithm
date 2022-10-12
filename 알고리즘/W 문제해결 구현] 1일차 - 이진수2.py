T=int(input())
for t in range(1,T+1):
    q=float(input())
    a=''
    n=0
    while True:
        n+=1
        if 0.5**n>q:
            a+='0'
        else:
            a+='1'
            q=q-0.5**n
        if q==0:
            break
    if n>12:
        a='overflow'
    print(f'#{t} {a}')