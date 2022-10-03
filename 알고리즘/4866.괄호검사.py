
T = int(input()) #print('{} {}'.format(1, 2))

for tc in range(1,1+T):
    lst=input()
    stack=[]
    result = 1

    for i in lst:
        if len(stack)==0:
            if i =='}' or i ==')':
                result=0
                break
            elif i=='{' or '(':
                stack.append(i)
        else:
            if stack[-1]== '(' and i == ')':
                stack.pop()
                continue
            elif stack[-1] == '{' and i =='}':
                stack.pop()
                continue
            elif i == '(' or i =='{':
                stack.append(i)
            elif i== ')' or i =="}":
                result = 0
                break
    if stack:
        result=0

    print(f'#{tc} {result}')
