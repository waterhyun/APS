# 돌을 놓는 함수
def place_stone(x, y, c):
    global grid, dx, dy
    grid[x][y] = c
    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        stones_to_flip = []
        while 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 3 - c:
            stones_to_flip.append((nx, ny))
            nx += dx[d]
            ny += dy[d]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == c:
            for fx, fy in stones_to_flip:
                grid[fx][fy] = c


tc = int(input())
for t in range(1, tc+1):
    n, m = map(int,input().split())
    grid = [[0] * n for i in range(n)]
    grid[(n//2) - 1][n//2] = grid[n//2][(n//2) - 1] = 1  # 'B'
    grid[(n//2) - 1][(n//2) - 1] = grid[n//2][n//2] = 2  # 'W'

    dx = [0, 0, 1, -1, 1, -1, -1, 1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]

    for turn in range(m):
        x, y, c = map(int, input().split())
        x -= 1
        y -= 1
        if grid[x][y] == 0:
            place_stone(x, y, c)

    # 돌의 개수
    cnt_b = sum(row.count(1) for row in grid)
    cnt_w = sum(row.count(2) for row in grid)

    print(f"#{t} {cnt_b} {cnt_w}")