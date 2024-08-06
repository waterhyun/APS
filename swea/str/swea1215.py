# [S/W 문제해결 기본] 3일차 - 회문1

for t in range(1, 11):
    n = 8
    m = int(input())
    arr = [input() for i in range(n)]
 
    cnt = 0
    result = ""
    # 행에서 회문 찾기
    for idx in range(n):
        start = 0
        while start <= n - m:
            sub_str = arr[idx][start:start + m]
            if sub_str == sub_str[::-1]:
                cnt += 1
            start += 1
 
    # 열에서 회문 찾기
    for col in range(n):
        start = 0
        col_str = ''.join(arr[row][col] for row in range(n))
        while start <= n - m:
            sub_str = col_str[start:start + m]
            if sub_str == sub_str[::-1]:
                cnt += 1
            start += 1
 
    print(f'#{t} {cnt}')