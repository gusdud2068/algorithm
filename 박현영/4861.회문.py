T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxN 크기의 글자판, 길이가 M 인 회문
    arr = [input() for _ in range(N)]  # N 개의 글자로 이루어진 N 개의 줄 입력
    result = ''
for i in range(N):
    for j in range(N - M + 1):  # 인덱스 범위 조심
        word_row = ''
        for k in range(M):
            word_row += arr[i][j + k]
            # 만든 단어, 거꾸로 뒤집은 단어 비교
            # 일치하는 답을 찾았으면 result 바꾸기
            if arr[i][j + k] != arr[i][j + M - k - 1]:
                break
            # 일치하는 답을 찾았다. k 가 M-1 이 되었을 때
            if k == M - 1:
                result = word_row

        # 세로로 검사
        word_col = ''
        for k in range(M):
            word_col += arr[j + k][i]
            if arr[j + k][i] != arr[j + M - k - 1][i]:
                break
            if k == M - 1:
                result = word_col
print(f'#{tc} {result}')


# 3143
# 4865


# 1
# 10 10
# GOFFAKWFSM
# OYECRSLDLQ
# UJAJQVSYYC
# JAEZNNZEAJ
# WJAKCGSGCF
# QKUDGATDQL
# OKGPFPYRKQ
# TDCXBMQTIO
# UNADRPNETZ
# ZATWDEKDQF
