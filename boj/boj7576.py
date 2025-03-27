# 토마토

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

flat_graph = sum(graph, [])
if all(x == 1 or x == -1 for x in flat_graph):
    if all(x == 1 for x in flat_graph):
        print(0)
    else:
        print(-1)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q.append((i, j, 0))
                
    max_days = 0
    while q:
        i, j, days = q.popleft()
        max_days = max(max_days, days)
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 0:
                graph[ni][nj] = 1
                q.append((ni, nj, days + 1))
                
    for row in graph:
        if 0 in row:
            print(-1)
            return
    print(max_days)

bfs()



# import sys
# from collections import deque
# input = sys.stdin.readline

# M, N = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]

# flat_graph = sum(graph, [])
# if all(x == 1 or x == -1 for x in flat_graph):
#     if all(x == 1 for x in flat_graph):
#         print(0)
#     else:
#         print(-1)

# directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# # 하루 동안 일어나는 거
# def bfs():
#     q = deque()
#     for i in range(N):
#         for j in range(M):
#             if graph[i][j] == 1:
#                 q.append((i, j, 0))
    
#     max_days = 0
#     while q:
#         i, j, days = q.popleft()
#         max_days = max(max_days, days)

#         for di, dj in directions:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 0:
#                 graph[ni][nj] = 1
#                 q.append((ni, nj, days + 1))

#     for row in graph:
#         if 0 in row:
#             print(-1)
#             return
#     print(max_days)

# # def bfs(graph, si, sj):
# #     visited = [[False] * M for _ in range(N)]
# #     visited[si][sj] = True
# #     q = deque()
# #     q.append((si, sj))
    
# #     while q:
# #         si, sj = q.popleft()
# #         for di, dj in directions:
# #             ni, nj = si + di, sj + dj
# #             if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and graph[ni][nj] == 0:
# #                 graph[nj][nj] = 1
# #                 visited[ni][nj] = True
# #                 q.append((ni, nj))

# #     return graph

# # 토마토가 모두 익을 수 있는지 없는지 판단하는 과정
# def dfs(si, sj):
#     stack = [(si, sj)]
#     visited[si][sj] = True
#     has_ripe = False

#     while stack:
#         i, j = stack.pop()
#         if graph[i][j] == 1:
#             has_ripe = True

#         for di, dj in directions:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
#                 if graph[ni][nj] != -1:
#                     visited[ni][nj] = True
#                     stack.append((ni, nj))
    
#     return has_ripe

# visited = [[False] * M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 0 and not visited[i][j]:
#             if not dfs(i, j):
#                 print(-1)

