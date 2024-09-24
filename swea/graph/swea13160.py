# 13160. 5250. 최소 비용 (제출용)

import sys
sys.stdin = open('swea/input.txt', 'r')

import heapq


def dijkstra(grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 거리 배열 초기화
    distances = [[float('inf')] * n for _ in range(n)]

    # 시작 0
    distances[0][0] = 0

    # 우선순위 큐
    pq = [(0, 0, 0)] # (연료 소비량, 행, 열)

    while pq:
        fuel, r, c = heapq.heappop(pq)

        # 목적지에 도착한 경우
        if r == n-1 and c == n-1:
            return fuel
        
        # 현재 위치의 연료 소비량이 이미 알려진 최소값 보다 클 경우
        if fuel > distances[r][c]:
            continue

        # 인접한 칸 탐색
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n:
                # 인접 지역 이동시 1만큼 연료 들고
                # 더 높은 곳으로 이동하는 경우, 높이 차이만큼 추가로 연료가 소비
                new_fuel = fuel + 1 + max(0, grid[nr][nc] - grid[r][c])
                
                if new_fuel < distances[nr][nc]:
                    distances[nr][nc] = new_fuel
                    heapq.heappush(pq, (new_fuel, nr, nc))

        
    # 도달할 수 없는 경우
    return -1 



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    result = dijkstra(grid)
    print(f'#{tc} {result}')

