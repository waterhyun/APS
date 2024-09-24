import sys
sys.stdin = open('swea/input.txt', 'r')
import heapq


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}  # 누적 거리 저장할 테이블
    distances[start] = 0
    queue = [(0, start)]  # 단 방향 그래프

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            return current_distance

        # 가중치가 더 큰 경우
        if current_distance > distances[current_node]:
            continue
        

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 다음 노드를 가는 데 더 많은 비용이 많이 들지 않은 경우
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return float('inf')

T = int(input())
for tc in range(1, T+1):
    # 마지막 연결지점 번호, 도로의 개수
    N, E = map(int, input().split())
    # 그래프를 딕셔너리 형태로 구성
    # 키 = 노드, 값 = 이웃 노드(키)와 거리(값)
    graph = {i: {} for i in range(N + 1)}

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    
    # print(graph)

    result = dijkstra(graph, 0, N)
    print(f'#{tc} {result}')
