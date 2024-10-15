# 도시 건설 - 프림 알고리즘 사용
import sys
sys.stdin = open('boj/input.txt', 'r')

import heapq

# 최소 비용 신장 트리의 경우 cost가 먼저 들어옴

# def prim(graph, n):
def prim(graph, start):
    # 최소 비용
    mst_cost = 0
    # visited = [False] * (n+1)
    visited = set([start])
    # pq = [(0, 1)] # cost, node  # 시작점의 가중치는 0, 1번 노드부터 시작
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)
    # print(f'edges: {edges}')

    # while edges:
    #     cost, node = heapq.heappop(pq)

    #     # 이미 방문한 지점이면 통과
    #     if visited[node]:
    #         continue
        
    #     # 처음 방문한 곳
    #     # 방문처리하기
    #     visited[node] = True
    #     # 비용 구하기
    #     mst_cost += cost

    #     # 다음 인접 노드 중 방문하지 않은 곳 탐색
    #     for next_node, next_cost in graph[node]:
    #         if not visited[next_node]:
    #             # 추가
    #             heapq.heappush(pq, (next_cost, next_node))
    
    # if all(visited[1:]):
    #     return mst_cost
    # else:
    #     return -1

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst_cost += cost
            for next_to, next_cost in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))

    return mst_cost if len(visited) == len(graph) else -1



# 건물의 개수, 도로의 개수
N, M = map(int, input().split())

# 인접리스트 만들기
# graph = [[] for _ in range(N + 1)]
# 딕셔너리로 표현하기
graph = {i: {} for i in range(1, N+1)}


total_cost = 0
# 건물의 번호 a, b와 두 건물 사이 도로를 만들 때 드는 비용 c
for _ in range(M):
    start, to, cost = map(int, input().split())
    # graph[start].append((to, cost))  # 연결된 노드와 비용(가중치)
    # graph[to].append((start, cost))  # 무방향 그래프
    graph[start][to] = cost
    graph[to][start] = cost
    total_cost += cost  # 도로 다 설치할 때 드는 비용

# print(graph)

# min_cost = prim(graph, N)
min_cost = prim(graph, 1)
if min_cost == -1:
    print(-1)
else: 
    # 얼마나 절약 되는지 계산하기
    print(total_cost - min_cost)


