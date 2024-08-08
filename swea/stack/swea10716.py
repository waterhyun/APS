# 4874. [기본] 5일차 - Forth (제출용) D1

# 테스트 케이스
tc = int(input())
for t in range(1, tc+1):
    expression = list(input().split())
    stack = []
    for i in expression:
        if i.isdigit(): # 피연산자
            stack.append(i)
        elif i == '.': # 마지막
            if len(stack) != 1: # 출력할 결과가 없거나, 남은 숫자가 1개를 넘어갈 경우
                print(f'#{t} error')
            else:
                print(f'#{t} {result}')
        else:
            if len(stack) >= 2: # 2개 숫자 필요
                if stack[-1].isnumeric() and stack[-2].isnumeric(): # 숫자 인지 아닌지 확인
                    a = stack.pop() # 스택에서 제거
                    b = stack.pop() # 스택에서 제거
                    if i == '+':
                        result = int(b) + int(a)
                    elif i == '/':
                        result = int(int(b) / int(a))
                    elif i == '*':
                        result = int(b) * int(a)
                    elif i == '-':
                        result = int(b) - int(a)
                    stack.append(str(result)) # 결과 스택에 저장
                else:
                    print(f'#{t} error')
                    break
            else:
                print(f'#{t} error')
                break