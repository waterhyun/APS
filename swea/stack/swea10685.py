#  4873. [기본] 4일차 - 반복문자 지우기 (제출용)

def my_push(item):
    global stack, top
    top += 1
    stack[top] = item

def my_pop():
    global top
    if top == -1:
        return False
    top -= 1

def length(string):
    global stack, top
    stack = [0]*len(string)
    top = 0
    for s in string:
        if s != stack[top]:
            my_push(s)
        else:
            if s == stack[top]:
                my_pop()
     
    return top


tc = int(input())
for t in range(1, tc+1):
    string =  input()
    result = length(string)
    print(f'#{t} {result}')

##################################

T = int(input())
for tc in range(1, T+1) :
    string = list(input())
    stack = [string.pop(0)]
    top = 1
    while string:
        s = string.pop(0)
        if stack :
            if stack[top-1] != s:
                stack.append(s)
                top += 1
            elif stack[top-1] == s:
                top -= 1
                stack.pop()
        else :
            stack.append(s)
            top += 1
    print(f'#{tc} {len(stack)}')