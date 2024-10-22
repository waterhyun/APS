# 다리 만들기
import sys
sys.stdin = open('boj/input.txt', 'r')


from collections import deque

# 섬 구분하기
def labeling(x, y, label):
    q = deque([(x, y)])
    map_grid[x][y] = label
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < N and map_grid[nx][ny] == 1:
                map_grid[nx][ny] = label
                q.append((nx, ny))

def clustering(map_grid):
    label = 2
    for i in range(N):
        for j in range(N):
            if map_grid[i][j] == 1:
                labeling(i, j, label)
                label += 1

# 최단 거리 찾기

def find(start_points, label):
    min_distance = 1e9
    q = deque(start_points)
    distance = [[-1]*N for _ in range(N)]
    for sx, sy in start_points:
        distance[sx][sy] = 0

    while q:
        cx, cy = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < N:
                # 바다이면서, 아직 방문하지 않은 곳(다리를 짓지 않은 곳)
                if map_grid[nx][ny] == 0 and distance[nx][ny] == -1:
                    # 다리를 만들고, 거리 + 1
                    distance[nx][ny] = distance[cx][cy] + 1
                    q.append((nx, ny))
                # 섬에 방문했고, 그 섬이 내 섬과 다를 경우
                elif map_grid[nx][ny] > 1 and map_grid[nx][ny] != label:
                    # print(f'map_grid[nx][ny]:{map_grid[nx][ny]}, map_grid[cx][cy]:{map_grid[cx][cy]}')
                    min_distance = min(min_distance, distance[cx][cy])          
    # for row in distance:
    #     print(row)
    # print()
    return min_distance

# 입력
N = int(input())
map_grid = [list(map(int, input().split()))for _ in range(N)]
clustering(map_grid)
# for row in map_grid:
#     print(*row)

result = 1e9

for label in range(2, max(map(max, map_grid)) + 1):
    start_points = [(i, j) for i in range(N) for j in range(N) if map_grid[i][j] == label]
    result = min(result, find(start_points, label))

print(result)


# from collections import deque

# def bfs_label_islands(grid, n):
#     label = 2
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
#     def bfs(x, y):
#         queue = deque([(x, y)])
#         grid[x][y] = label
#         while queue:
#             cx, cy = queue.popleft()
#             for dx, dy in directions:
#                 nx, ny = cx + dx, cy + dy
#                 if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
#                     grid[nx][ny] = label
#                     queue.append((nx, ny))

#     for i in range(n):
#         for j in range(n):
#             if grid[i][j] == 1:
#                 bfs(i, j)
#                 label += 1

# def bfs_shortest_bridge(grid, n):
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     min_distance = float('inf')
    
#     def bfs(start_points):
#         nonlocal min_distance
#         queue = deque(start_points)
#         distance = [[-1] * n for _ in range(n)]
        
#         for x, y in start_points:
#             distance[x][y] = 0
        
#         while queue:
#             x, y = queue.popleft()
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if grid[nx][ny] == 0 and distance[nx][ny] == -1:
#                         distance[nx][ny] = distance[x][y] + 1
#                         queue.append((nx, ny))
#                     elif grid[nx][ny] > 1 and grid[nx][ny] != grid[x][y]:
#                         min_distance = min(min_distance, distance[x][y])
#                         return

#     for label in range(2, max(map(max, grid)) + 1):
#         start_points = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == label]
#         bfs(start_points)
    
#     return min_distance

# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# bfs_label_islands(grid, n)
# result = bfs_shortest_bridge(grid, n)
# print(result)
