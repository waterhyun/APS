# 2001. 파리 퇴치

def f(arr, x, y, n, m):
    cnt = 0
    for i in range(x, x+m):
        for j in range(y, y+m):
            if 0 <= i < n and 0 <= j < n:
                cnt += arr[i][j]

    return cnt

tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = f(arr, i, j, n, m)
            if max_v < cnt:
                max_v = cnt

    print(f'#{t} {max_v}')

#################

def f(arr, x, y, m):
    return sum(sum(arr[i][y:y+m]) for i in range(x, x+m))

tc = int(input())  # 테스트 케이스 개수 입력
for t in range(1, tc+1):
    n, m = map(int, input().split())  
    arr = [list(map(int, input().split())) for _ in range(n)]  

    max_v = 0  
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = f(arr, i, j, m) 
            if max_v < cnt:
                max_v = cnt  

    print(f'#{t} {max_v}')  
