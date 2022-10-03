def comb():
    # 부분집합 구하기
    for i in range(1 << N): #1000000
        set1 = set()
        for j in range(N): #0 1 2 3 4 5
            if i & (1 << j): # 1 10 100 1000 10000 100000 & 1000000
                set1.add(j)

        if len(set1) == N2:        # 갯수가 N2개인 조합
            combi.add(tuple(set1))

        comb2.add(tuple(set1)) #부분집합


#리스트 중에 3개의 음식재로로 뽑을 수있는 겹칠수도 있는 모든 경우의 수 (순열)
#리스트중에 3개의 음식재료로 뽑을 수 있는 겹치지 않는 모든 경우의 수를 구하시오 (조합)
#리스트중에서 만들 경우의 수 다 뽑아내기 (부분집합)

lst=["사과","바나나","배","소금","간장","설탕"]
N = int(input()) #6 a b c d e f
N2 = int(input()) #3

combi = set()
comb2 = set()

comb()

print(combi)

#print(comb2)