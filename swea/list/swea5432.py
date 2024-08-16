# 5432. 쇠막대기 자르기

tc = int(input()) # 테스트케이스
for t in range(1, tc+1):
    arr = list(input())
    result = 0
    cnt = 0
    i = 0
    while i < len(arr):
        if arr[i] == '(' and arr[i+1] == ')':
            result += cnt
            i += 2
            continue
        elif arr[i] == '(':
            cnt += 1
            i += 1
            continue
        elif arr[i] == ')':
            result += 1
            cnt -= 1
            i += 1

    print(f'#{t} {result}')

