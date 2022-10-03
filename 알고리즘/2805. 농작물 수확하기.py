T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    arr1 = [list(map(int, input())) for _ in range(n)]

    i=n//2
    j=n//2

    sum1=0
    for x in range(n):
        for y in range(n):
          if abs(x-i)+abs(y-j)<=n//2:
              sum1+=arr1[x][y]
    print(sum1)
