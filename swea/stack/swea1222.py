# [S/W 문제해결 기본] 6일차 - 계산기1 D4

for t in range(1, 11):
    size = int(input())
    expre = input()
    stack = []
    total = 0
    for e in expre:
        if ord(e) in range(48, 58): # 피연산자
            stack.append(int(e))
        else:
            total += stack.pop()
    total += int(e)
     
    print(f'#{t} {total}')


# def find_order(top, s):
#     # 스택 안에 있는 것의 우선순위
#     isp = {0:['('], 1:{'+', '-'}, 2:{'*', '/'}}
#     # 스택 밖에 있는 것의 우선순위
#     icp = {1:{'+', '-'}, 2:{'*', '/'}, 3:['(']}
#     # ')'일 경우 '('을 만나기 까지 pop
    
#     for key, value in isp.items():
#         if top in value:
#             isp_value = key
#     for key, value in icp.items():
#         if s in value:
#             icp_value = key
#     return isp_value, icp_value

# top = '('
# s = '+'
# a, b = find_order(top, s)
# print(a, b)
# def postfix(expr):
#     stack = []
#     result = ''
#     # 스택 안에 있는 것의 우선순위
#     isp = {0:['('], 1:{'+', '-'}, 2:{'*', '/'}}
#     # 스택 밖에 있는 것의 우선순위
#     icp = {1:{'+', '-'}, 2:{'*', '/'}, 3:['(']}

#     # 피연산자 인지, 연산자 인지 나누기
#     for e in expr:
#         if ord(e) in range(48, 58): # 피연산자
#             result += e
#         else:
#             # 연산자
#             # 들어 온 연산자의 우선순위 파악하기
#             if e == ')':
#                 # '('일때 까지 pop
#                 while stack[-1] != '(':
#                     p = stack.pop()
#                     result += p
#                     break
#                 p = stack.pop()
#                 result += p
#             else:
#                 for key, value in icp.items():
#                     if e in value:
#                         icp_value = key                      
#                 for key, value in isp.items():
#                     if stack == []:
#                         # 빈 경우
#                         stack.append(e)
#                     elif stack[-1] in value:
#                         isp_value = key
#                         # isp 값과 icp 값 비교해서 높으면 push
#                         if isp_value < icp_value:
#                             stack.append(e)
#                         # 스택의 top이 더 크거나 같으면 pop
#                         elif isp_value >= icp_value:
#                             p = stack.pop()
#                             result += p
#     return result

# string = '9+8+5+9+2+4+1+8+3+9+3+8+7+8+6+8+9+4+1+1+7+6+1+5+8+7+6+9+6+3+1+3+1+7+5+9+2+8+4+3+7+3+4+7+3+4+8+3+2+6+6'
# result = postfix(string)
# print(result)   



