# 최소 스패닝 트리

import sys
sys.stdin = open('boj/input.txt', 'r')

import heapq

def prim(start):
    heap = list()
    # MST = [0] * (V+1)
    MST = set()

    sum_weight = 0
    heapq.heappush(heap, (0, start))

    while heap and len(MST) < V:
        w, s = heapq.heappop(heap)

        if s in MST:
            continue

        MST.add(s)
        sum_weight += w
        
        # for t in range(1, V+1):
        #     if graph[s][t] == 0 :
        #         continue
        #     if MST[t]:
        #         continue
        #     heappush(heap, (graph[s][t], t))

        # print(graph[s].items())
        for t, ww in graph[s].items():
            if t in MST:
                continue
            heapq.heappush(heap, (ww, t))
    
    return sum_weight


V, E = map(int, input().split())
# graph = [[0] * (V+1) for _ in range(V+1)]
graph = {i: {} for i in range(1, V+1)}

for i in range(E):
    start, to, weight = map(int, input().split())
    graph[start][to] = weight
    graph[to][start] = weight

# print(graph)
print(prim(start))


# --------


import sys
import heapq

def prim(start):
    mst = set()
    edges = [(0, start)]
    total_weight = 0

    while edges and len(mst) < V:
        weight, node = heapq.heappop(edges)
        if node not in mst:
            mst.add(node)
            total_weight += weight
            for next_node, next_weight in graph[node]:
                if next_node not in mst:
                    heapq.heappush(edges, (next_weight, next_node))

    return total_weight


V, E = map(int, sys.stdin.readline().split())
graph = [[] * (V+1) for _ in range(V+1)]

for _ in range(E):
    start, to, weight = map(int, sys.stdin.readline().split())
    graph[start].append((to, weight))
    graph[to].append((start, weight))


print(prim(1))
