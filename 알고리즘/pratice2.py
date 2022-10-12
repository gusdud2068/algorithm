def postorder(node):
    if node>N or lst[node] != 0:
        return

    left = node*2
    right=node*2+1
    postorder(left)
    postorder(right)
    lst[node]=lst[left]+lst[right]


T = int(input())
for tc in range(1,1+T):
    N,M,L = map(int,input().split()) #노드 개수 리프노드의 개수 값을 출력할 노드
    leaf = [list(map(int,input().split())) for _ in range(M)]
    lst = [0]*(N+2) #양쪽 자식
    for i in range(M):
        lst[leaf[i][0]] = leaf[i][1]

    postorder(1)
    print(f'#{tc} {lst[L]}')
