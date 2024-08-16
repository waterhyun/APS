# 풍선팡 D2

di = [0, 1, 0, -1]
dj = [1, 0 ,-1, 0]

tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split()) # 행, 열 크기
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0 # 꽃가루 최대 합계
    for i in range(n): # 터트려볼 풍선의 위치
        for j in range(m):
            cnt = arr[i][j]
            for k in range(4): # 확인할 방향
                for l in range(1, arr[i][j]+1): # 주변 방향으로 추가로 터지는 풍선과의 거리
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < n and 0 <= nj < m:
                        cnt += arr[ni][nj] # 주변의 풍선에서 나오는 꽃가루 추가
            
            if max_v < cnt: #for k에서 모든 꽃가루가 더해졌기 때문에
                max_v = cnt
    
    print(f'#{t} {max_v}')