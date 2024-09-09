import sys
sys.stdin = open('swea/input.txt', 'r')


# +
def plus_spray(x, y, M):
    fly_cnt = grid[x][y]
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        for step in range(1, M):
            nx = x + (dx * step)
            ny = y + (dy * step)
            if 0 <= nx < N and 0 <= ny < N: 
                fly_cnt += grid[nx][ny]
    return fly_cnt

# x
def x_spray(x, y, M):
    fly_cnt = grid[x][y]
    for dx, dy in [(-1, 1), (1, 1), (1, -1), (-1, -1)]:
        for step in range(1, M):
            nx = x + (dx * step)
            ny = y + (dy * step)
            if 0 <= nx < N and 0 <= ny < N: 
                fly_cnt += grid[nx][ny]
    return fly_cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            # print(plus_spray(i, j, M), x_spray(i, j, M), max_v)
            max_v = max(plus_spray(i, j, M), x_spray(i, j, M), max_v)
    print(f'#{tc} {max_v}')
