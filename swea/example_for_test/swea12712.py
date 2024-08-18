tc = int(input())

di_p = [0, 1, 0, -1]
dj_p = [1, 0, -1, 0]
di_x = [1, 1, -1, -1]
dj_x = [1, -1, 1, -1 ]
for t in range(1, tc+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    value = 0
    for i in range(N):
        for j in range(N):
            value_p = grid[i][j]
            value_x = grid[i][j]
            for k in range(4):
                for s in range(1, M):
                    ni_p = i + di_p[k] * s
                    nj_p = j + dj_p[k] * s
                    if 0 <= ni_p < N and 0 <= nj_p < N:
                        value_p += grid[ni_p][nj_p]
                for s in range(1, M):
                    ni_x = i + di_x[k] * s
                    nj_x = j + dj_x[k] * s
                    if 0 <= ni_x < N and 0 <= nj_x < N:
                        value_x += grid[ni_x][nj_x]
            
            value = max(value_p, value_x, value)
    
    print(f'#{t} {value}')
