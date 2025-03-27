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

