T = int(input())

#operation = {'+': 1, '-': 1, '*': 2, '/': 2}

for t in range(1, T + 1):

    infix = input().split() #넣을문자열

    stack = []
    result = 0

    for i in infix:# 문자열 하나하나
        if i == ".":
            break
        elif i.isdigit():
            stack.append(i)
            continue
        else: #연산자가 나온다면
            if len(stack) == 1:
                result = 'error'
                break
            right = int(stack.pop()) #2
            left = int(stack.pop()) #10
            if i == "+":
                result= left + right
            elif i == "-":
                result= left - right
            elif i == "/":
                result = left // right
            elif i== "*":
                result = left*right
            stack.append(result)
    if len(stack)>1:
        result = 'error'
    print(f'#{t} {result}')


