T = 10

icp = {'+': 1, '*': 2}
for tc in range(1, 1 + T):
    n = int(input())  # 식의 길이 101

    exp = input()  # 중위표현식입력받음9+5*2+1+3*3*7*6*9*1*7+1+8*6+6*1*1*5*2*4*7+4*3*8*2*6+7*8*4*5+3+7+2+6+5+1+7+6+7*3*6+2+6+6*2+4+2*2+4*9*3
    postfix = ""  # 후위표현식으로 바꾼 결과

    stack = []

    for i in range(n):
        # 글자를 하나씩 때서 보는데
        # 연산자 or 피연산자

        if "0" <= exp[i] <= "9":
            # 피연산자면 그냥 결과 문자열에 이어 붙이기
            postfix += exp[i]  # 숫자
        else:
            # 연산자면 스택의 꼭대시(top)을 확인해서 자신보다 같거나 높은 우선순위를 가진 연산자가 있으면 꺼낸다.
            if stack and icp[stack[-1]] >= icp[exp[i]]:
                postfix += stack.pop()
            stack.append(exp[i])

    # 스택이 남아있는 연산자는 뒤에 붙이기
    while stack:
        postfix += stack.pop()

        # 후위표기식 계산
    result = 0
    stack = []
    k = len(postfix)
    for i in range(k):
        # 피연산자가 나오면 그냥 넘어가고
        # 스택에다가 담는다.
        if "0" <= postfix[i] <= "9":
            stack.append(postfix[i])
        else:
            # 연산자가 나오면 계산 (앞에 두 피연산자를 선택)
            # 스택에서 두개의 피연산자를 꺼낸다.
            right = int(stack.pop())
            left = int(stack.pop())

            if postfix[i] == "+":
                result = right + left
            else:
                result = right * left

            stack.append(result)  # 계산하고 그 결과를 스택에 다시 넣어주기(차후를 위해)

    print(f'#{tc} {result}')
    print(postfix)