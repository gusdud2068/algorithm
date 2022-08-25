T = int(input())

for tc in range(1, T+1):
    n = int(input()) #숫자길이
    lst = list(map(int, input().split()))
    # 버블 정렬
    # 앞에서부터 2개씩 비교, 비교 후 앞의 것이 크면 서로 교환
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(f'#{tc}', end=' ')
    for e in lst:
        print(e, end=' ')
    print()