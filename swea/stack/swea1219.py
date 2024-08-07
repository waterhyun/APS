# [S/W 문제해결 기본] 4일차 - 길찾기 D4
def dfs(graph, start, end):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            return 0
        if node not in visited:
            if node == end:
                return 1
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

for _ in range(10):
    t, E = map(int, input().split())        # 테스트 케이스의 번호, 길의 총 개수
    arr = list(map(int, input().split()))   # 순서쌍 입력
    data_table = [[] for _ in range(100)]
    for i in range(0, E*2, 2):
        data_table[arr[i]].append(arr[i+1])
    result = dfs(data_table, 0, 99)
    if result == 1:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')