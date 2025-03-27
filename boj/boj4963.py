# 섬의 개수
# import sys
# input = sys.stdin.readline


# import sys
# sys.setrecursionlimit(10**6)  # 재귀 깊이 증가

directions = [(0, 1), (1, 0), (-1, 0), (0, -1),
              (1, 1), (1, -1), (-1, -1), (-1, 1)]

def dfs(i, j):
    stack = [(i, j)]
    visited[i][j] = 1  # 방문 처리

    while stack:
        x, y = stack.pop()
        for di, dj in directions:
            ni, nj = x + di, y + dj
            if 0 <= ni < h and 0 <= nj < w and graph[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                stack.append((ni, nj))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 0  # 섬 개수 카운트
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:  # 새로운 섬을 발견했을 때
                dfs(i, j)
                cnt += 1  # 새로운 섬을 찾았으므로 증가

    print(f'resullt: {cnt}')





