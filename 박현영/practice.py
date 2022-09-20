def inorder(node):  # 중위 preorder 전 post후
    global number

    if node > N:
        return
    left = node * 2
    right = node * 2 + 1

    inorder(left)
    lst[node] = number
    number += 1
    inorder(right)


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    lst = [0] * (N + 1)  # 7
    number = 1

    inorder(1)
    print(f'#{tc} {lst[1]} {lst[N//2]}')