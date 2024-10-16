import sys
sys.stdin = open('boj/input.txt', 'r')


import heapq

# 시작 정점, 인접 정점, 거리
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    path = []

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        path.append(now)
        for next_node, next_cost in graph[now]:
            new_cost = dist + next_cost

            if new_cost >= distance[next_node]:
                continue

            # print(f'new_cost: {new_cost}, next_node: {next_node}')
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

    return path

N, M = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
# print(*graph, end='\n')
for _ in range(M):
    start, to, weight = map(int, input().split())
    # print(start, to, weight)
    graph[start].append((to, weight))
    graph[to].append((start, weight))


# 모든 노드로 가기 위한 최단 거리 출력
result = [['-']*N for _ in range(N)]
for i in range(1, N+1):
    distance = [1e9] * (N+1)
    path = dijkstra(i)
    print(f'start:{i},', end=' ')
    for j in range(1, N+1):
        # 도달할 수 없는 경우, 무한 출력
        if distance[j] == 1e9:
            print("INF", end=' ')
        else:
            print(distance[j], end=' ')

    print(f'경로: {path}')

    for ind in range(1, len(path)):
        if result[i-1][path[ind]-1] == '-':
            result[i-1][path[ind]-1] = path[ind-1]

# print(*result, end='\n')

# start:1, 0 2 1 5 5 7 경로: [1, 3, 2, 4, 5, 6]
# start:2, 2 0 3 5 3 5 경로: [2, 1, 3, 5, 4, 6]
# start:3, 1 3 0 4 6 7 경로: [3, 1, 2, 4, 5, 6]
# start:4, 5 5 4 0 6 4 경로: [4, 3, 6, 1, 2, 5]
# start:5, 5 3 6 6 0 2 경로: [5, 6, 2, 1, 3, 4]
# start:6, 7 5 7 4 2 0 경로: [6, 5, 4, 2, 1, 3]

############


# n, m = map(int, input().split())
# dist = [[1e9] * (n+1) for _ in range(n+1)]
# result = [[0] * (n+1) for _ in range(n+1)]

# for _ in range(m):
#     start, to, weight = map(int, input().split())
#     dist[start][to] = dist[to][start] = weight
#     result[start][to] = to
#     result[to][start] = start

# # print('## dist ##')
# # for i in range(1, n+1):
# #     for j in range(1, n+1):
# #         if dist[i][j] == 1e9:
# #             print('INF', end= " ")
# #         else:
# #             print(dist[i][j], end=" ")
# #     print()

# # print('## result - before ##')
# # for i in range(1, n+1):
# #     for j in range(1, n+1):
# #         if i == j:
# #             print("-", end=" ")
# #         else:
# #             print(result[i][j], end=" ")
# #     print()


# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if dist[i][j] > dist[i][k] + dist[k][j]:
#                 dist[i][j] = dist[i][k] + dist[k][j]
#                 result[i][j] = result[i][k]

# # print('## result - after ##')
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             print("-", end=" ")
#         else:
#             print(result[i][j], end=" ")
#     print()
