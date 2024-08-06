# 4861. [기본] 3일차 - 회문 (제출용) D2

tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    arr = [input() for i in range(n)]
 
    result = ""
    # 행에서 회문 찾기
    for idx in range(n):
        start = 0
        while start <= n - m:
            sub_str = arr[idx][start:start + m]
            if sub_str == sub_str[::-1]:
                result = sub_str
                break
            start += 1
        if result:
            break
 
    # 열에서 회문 찾기 (행에서 찾지 못했을 경우)
    if not result:
        for col in range(n):
            start = 0
            col_str = ''.join(arr[row][col] for row in range(n))
            while start <= n - m:
                sub_str = col_str[start:start + m]
                if sub_str == sub_str[::-1]:
                    result = sub_str
                    break
                start += 1
            if result:
                break
 
    print(f'#{t} {result}')