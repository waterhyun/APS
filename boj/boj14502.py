# 연구소

import sys
sys.stdin = open('boj/input.txt', 'r')

N, M = map(int, input().split())
virus_position = []
grid = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j] == 2:
            virus_position.append((i, j))
    grid.append(arr)

# 세워야 하는 벽 3개
wall = 3

for i, j in virus_position:
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == 0:
            