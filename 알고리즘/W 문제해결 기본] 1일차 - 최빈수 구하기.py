t = int(input())

for tc in range(1, 1 + t):
    Tc = int(input())

    arr = list(map(int,input().split()))

    lst = [0] * 101


    for i in range(1000):
        lst[arr[i]] = lst[arr[i]]+1


    max1 = 0
    for j in range(101):
        if max1 <= lst[j]:
            max1 = lst[j]
            a=j

    print(f"#{Tc} {a}")
