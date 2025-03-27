# 트리의 지름

# 임의의 두 점 사의 거 중 가장 긴 것
import sys
input = sys.stdin.readline

# 입력
V = int(input().strip())
graph =[[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    i = 1
    while data[i] != -1:
        neighbor, weight = data[i], data[i+1]
        graph[node].append((neighbor, weight))
        i += 2

# 메서드 정의
def dfs(start):
    visited = [False]*(V+1)
    stack = [(start, 0)]
    
    visited[start] = True
    max_dist = 0
    last_node = start
    
    while stack:
        node, dist = stack.pop()
        
        if dist > max_dist:
            max_dist = dist
            last_node = node
            
        for next_node, w in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, dist+w))
                
    return max_dist, last_node

# 임의의 정점에서 시작해서 가장 먼 노드 찾기
_, last_node = dfs(1)

# 끝 노드에서 시작해서 가장 먼 노드간의 거리 찾기
result, _ = dfs(last_node)

print(result)


# # 입력
# V = int(input())
# graph =[[] for _ in range(V+1)]

# for _ in range(V):
#     data = list(map(int, input().split()))
#     node = data[0]
#     i = 1
#     while data[i] != -1:
#         neighbor, weight = data[i], data[i+1]
#         graph[node].append((neighbor, weight))
#         i += 2

# # 메서드 정의
# def dfs(v, dist):
#     global result, last_node
#     # 현재 노드를 방문 처리
#     visited[v] = True

#     # 최장 거리 갱신
#     if dist > result:
#         result = dist
#         last_node = v

#     for next_node, w in graph[v]:
#         # 만약 방문하지 않았다면 방문
#         if not visited[next_node]:
#             dfs(next_node, dist + w)

# # 임의의 정점에서 가장 먼 정점 찾기
# visited = [False] * (V+1)
# result, last_node = 0, 0
# dfs(1, 0)

# # 가장 먼 정점에서 다시 dfs 수행해서 트리의 지름 찾기
# visited = [False] * (V+1)
# result = 0
# dfs(last_node, 0)
# print(result)
