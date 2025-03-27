# 내리막길

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력 받기
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]  # -1: 아직 방문 X, 0 이상: 저장된 경로 개수

# 방향 벡터 (우, 하, 좌, 상)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y):
    # 도착점 도달 시 경로 1개 추가
    if x == M - 1 and y == N - 1:
        return 1
    
    # 이미 계산된 경우 해당 값 반환 (메모이제이션)
    if dp[x][y] != -1:
        return dp[x][y]

    # 현재 좌표에서 시작하는 경로 개수 초기화
    dp[x][y] = 0

    # 4방향 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] < graph[x][y]:  # 내리막길 조건
            dp[x][y] += dfs(nx, ny)  # 가능한 모든 경로 합산

    return dp[x][y]

# 결과 출력
print(dfs(0, 0))

print(*dp, end=' ')

