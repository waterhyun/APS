# 미세먼지 확산
def dust(grid, R, C):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    new_grid = [[0]*C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                value = grid[i][j] // 5
                cnt = 0
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1:
                        new_grid[ni][nj] += value
                        cnt += 1
                new_grid[i][j] += grid[i][j] - (value * cnt)
            elif grid[i][j] == -1:
                new_grid[i][j] = -1
    
    return new_grid

# 공기청정기 작동 (방향에 따라)
def clean(cleaner, direction, grid, R, C):
    if direction == 'up':
        for i in range(cleaner - 1, 0, -1):
            grid[i][0] = grid[i-1][0]
        for i in range(C-1):
            grid[0][i] = grid[0][i+1]
        for i in range(cleaner):
            grid[i][C-1] = grid[i+1][C-1]
        for i in range(C-1, 1, -1):
            grid[cleaner][i] = grid[cleaner][i-1]
        grid[cleaner][1] = 0
    
    elif direction == 'down':
        for i in range(cleaner + 1, R - 1):
            grid[i][0] = grid[i+1][0]
        for i in range(C-1):
            grid[R-1][i] = grid[R-1][i+1]
        for i in range(R-1, cleaner, -1):
            grid[i][C-1] = grid[i-1][C-1]
        for i in range(C-1, 1, -1):
            grid[cleaner][i] = grid[cleaner][i-1]
        grid[cleaner][1] = 0

R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

# 공청기 위치 찾기
for i in range(R):
    if grid[i][0] == -1:
        cleaner_up = i
        cleaner_down = i + 1
        break

for _ in range(T):
    grid = dust(grid, R, C)  # 미세먼지 확산
    clean(cleaner_up, 'up', grid, R, C)  # 위쪽 공기청정기 작동
    clean(cleaner_down, 'down', grid, R, C)  # 아래쪽 공기청정기 작동

# 남은 미세먼지 합산
result = sum([g for gr in grid for g in gr if g > 0])
print(result)


# # 미세먼지 확산
# def dust(grid, R, C):

#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
    
#     new_grid = [[0]*C for _ in range(R)]

#     for i in range(R):
#         for j in range(C):
#             if grid[i][j] > 0:  # 미세먼지가 있다면
#                 # 확산될 공기 양 계산, 소수점은 버림
#                 value = grid[i][j] // 5 
#                 cnt = 0
#                 for d in range(4):
#                     # 인접한 네 방향으로 확산
#                     ni = i + di[d]
#                     nj = j + dj[d]
#                     if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1:
#                         # 확산되는 양
#                         new_grid[ni][nj] += value
#                         # 확산된 방향의 개수
#                         cnt += 1
#                 new_grid[i][j] += (grid[i][j] - (value * cnt))
#             if grid[i][j] == -1:
#                 new_grid[i][j] = -1

#     return new_grid

# # 위쪽 공기청정기
# def clean1():
#     for i in range(cleaner - 1, 0, -1):  # 아래로
#         grid[i][0] = grid[i-1][0]
#     for i in range(C-1):  # 왼쪽으로 
#         grid[0][i] = grid[0][i+1]
#     for i in range(cleaner):  # 위로
#         grid[i][C-1] = grid[i+1][C-1] 
#     for i in range(C-1, 1, -1):  # 오른쪽으로
#         grid[cleaner][i] = grid[cleaner][i-1]
#     grid[cleaner][1] = 0  # 공청기 바람

# def clean2():
#     for i in range(cleaner + 2, R - 1):  # 위로
#         grid[i][0] = grid[i+1][0]
#     for i in range(C-1):  # 왼쪽으로
#         grid[R-1][i] = grid[R-1][i+1]
#     for i in range(R - 1, cleaner + 1, -1):  # 아래로
#         grid[i][C-1] = grid[i - 1][C-1]
#     for i in range(C - 1, 1, -1):  # 오른쪽으로
#         grid[cleaner + 1][i] = grid[cleaner + 1][i-1]
#     grid[cleaner + 1][1] = 0  # 공청기 바람


# R, C, T  = map(int, input().split())  # R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000)

# # 격자판
# grid = [list(map(int, input().split())) for _ in range(R)]

# # 공청기가 있는 곳 찾기
# for i in range(R):
#     if grid[i][0] == -1:
#         # 항상 0열에 있으므로 첫 위치 발견하기
#         cleaner = i
#         break

# for _ in range(T):
#     grid = dust(grid, R, C)
#     clean1()
#     clean2()

# result = sum([g for gr in grid for g in gr if g > 0])
# print(result)
