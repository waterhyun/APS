# 4866. [기본] 4일차 - 괄호검사 (제출용)

def my_push(item):
    global top, stack
    top += 1
    stack[top] = item

def my_pop():
    global top
    if top == -1:
        return False
    top -= 1

def testing(string):
    global stack, top
    length = len(string)
    stack = [0]*length
    top = -1

    for s in string:
        if s in "({":
            my_push(s)
        elif s == ')' and top != -1 and stack[top] == '(':
            my_pop()
        elif s == '}' and top != -1 and stack[top] == '{':
            my_pop()
        elif s in ")}":
            return False

    return top == -1 and any(c in "(){}" for c in string)

# 테스트 케이스
tc = int(input())
for t in range(1, tc + 1):
    string = input().strip()
    if testing(string):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

##############################

def find_char(string, l) :
    char_d = {')' : '(' , '}' :'{'}
     
    for s in string :
        if s in char_d.values(): # 여는 괄호이면 추가
            l.append(s)
        elif s in char_d.keys()  : # 닫는 괄호이면
            if (not l) or (char_d[s] != l.pop()) : # 여는 괄호가 없거나, 짝이 맞지 않는 경우
                return 0
    if l : # 닫는 괄호가 없고 여는 괄호가 남아있는 경우
        return 0
    else :
        return 1
     
T =  int(input())
for tc in range(1, T+1) :
    string = str(input())
    lst = []
    result = find_char(string, lst)
    print(f'#{tc} {result}')

#######################################

T = int(input())
for tc in range(1, T+1) :
    string = list(input())
    lst = [0]*len(string)
    top = 0
    result = 1
    for s in string :
        if s == '(' or s == '{' :
            lst[top] = s
            top += 1
        elif s == ')' :
            top -= 1
            if lst[top] != '(' :
                result = 0
                break
        elif s == '}' :
            top -= 1
            if lst[top] != '{' :
                result = 0
                break
    if top != 0 :
        result = 0
 
    print(f'#{tc} {result}')


####################################
def check_bracket(str):
    stack = []
    # ( 혹은 { 라면 스택에 추가
    # } 면 스택 가장 마지막이 {인지 확인
    # ) 면 스택 가장 마지막이 (인지 확인
    for ch in str:
        if ch == '(' or ch == '{':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif ch == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0
    # 문자열을 다 돌았을 때 stack이 비어있어야 1
    if stack:
        return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    string = str(input())
    result = check_bracket(string)
    print(f'#{tc} {result}')