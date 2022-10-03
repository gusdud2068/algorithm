# 괄호가 없는 중위표기식

T = int(input())

operation = {'+': 1, '-': 1, '*': 2, '/': 2}

for t in range(1, T + 1):

    infix = input()

    postfix = ''

    stack = []

    for s in infix:

        if s >= '0' and s <= '9':  # 만약 s가 피연산자(숫자)이면..

            postfix += s  # 문자열에 그대로 붙여줍니다

        else:  # 만약 s가 연산자이면..

            if stack == []:  # 스택에 아무것도 없으면 그대로 push하고

                stack.append(s)

            else:  # 스택에 연산자가 존재한다면..

                while stack:  # push할때까지 반복하거나, stack에 연산자가 존재하지 않을 때까지 반복합니다.

                    if operation[stack[-1]] < operation[s]:  # 스택의 top의 우선순위보다 s의 연산 우선순위가 높으면

                        stack.append(s)
                        break  # push하는 순간 반복문을 탈출합니다.

                    else:  # 스택의 top의 우선순위가 더 높으면..

                        postfix += stack.pop()  # 연산자를 pop하여 문자열에 붙여줍니다.

                if stack == []:  # 만약 stack이 빌때까지 push하지 못하고 계속 pop을 수행했다면,

                    stack.append(s)

    # 중위표기식에 읽을 것이 없을 때, stack에 남아있는 모든 연산자를 pop하여 붙여줍니다.
    while stack:
