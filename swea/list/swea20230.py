# 20230. 풍선팡 보너스게임2


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

tc = int(input())  # 테스트 케이스
for t in range(1, tc+1):
    n = int(input())  # 격자 크기
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                for l in range(1, n): 
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < n and 0 <= nj < n:
                        cnt += arr[ni][nj] 
            
            if cnt > max_v:
                max_v = cnt
    
    print(f'#{t} {max_v}')

