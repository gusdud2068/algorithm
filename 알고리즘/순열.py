def perm(i):
    # p의 i번째 인덱스를 채우겠다
    if i == R:
        print(sorted(p))
        if sorted(p) not in ho:
            ho.append(sorted(p)[:])

    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i] = nums[j]
                perm(i+1)
                used[j] = 0


nums = [1, 3, 6, 4, 2]
N = len(nums)
R = 3

p = [0] * R
used = [0] * N
ho = []
perm(0)