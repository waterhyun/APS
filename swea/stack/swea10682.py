#  4871. [기본] 4일차 - 그래프 경로 (제출용) D3

def dfs(graph, start, end):
    visited = set()
    stack = [start]  # push 해놓고 시작
    while stack:
        node = stack.pop()  # pop
        if node not in visited:  # 한번도 방문하지 않았다면
            if node == end:
                return 1
            visited.add(node)  # 방문처리
            # push
            # graph[node] 인접한 노드 => neighbor
            # 만약 그 neighbor 가 방문하지 않았다면 push
            # 그 다음 다시 위로 올라가서 방문했는지 안 했는지 판단하면서 방문 처리
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return 0


tc = int(input())
for t in range(1, tc + 1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adjL[v1].append(v2)

    S, G = map(int, input().split())

    result = dfs(adjL, S, G)

    if result:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

