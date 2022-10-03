
T = int(input())


def binarySearch(a,N,key): # a=pagelist N=페이지갯수 key =구하고자하는답
    start = 0
    end = N-1
    cnt = 0
    while start <= end:
        middle = (start + end)//2
        cnt += 1
        if a[middle]==key:
            return cnt
        elif a[middle]>key:
            end = middle
        else:
            start=middle
    return False


for t in range(1,T+1): #def을 써서 A와 B결과 구한느곳
    P, Pa, Pb = map(int, input().split())

    a = [x for x in range(1,P+1)]

    A = binarySearch(a,P,Pa) #함수호출
    B = binarySearch(a,P,Pb)

    ans=0
    if A>B:
        ans = 'B'
    elif A==B:
        ans = '0'
    else:
        ans = "A"

    print(f'{t} {ans}')

