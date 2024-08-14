# 5102. 노드의 거리 (제출용) D3


# 주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
def BFS(t, start, goal):
    q = [(start, 0)]  # 현재 노드, 지나온 간선 개수 저장
    visited[start] = 1  # 시작 노드 방문 표시


    while q:  # 큐가 비어있지 않은 동안 실행
        now, cnt = q.pop(0)  # 큐에서 노드를 하나 꺼냄
        if now == goal:
            return print(f'#{t} {cnt}')

        for next in G[now]:
            # 현재 노드와 연결되어 있고, 아직 방문하지 않은 노드라면
            if visited[next] == 0:
                q.append((next, cnt + 1))  # 큐에 추가
                visited[next] = 1  # 방문 표시

    # 목표 노드에 도달할 수 없는 경우
    print(f'#{t} 0')


tc = int(input()) # 테스트 케이스
for t in range(1, tc+1):
    V, E = map(int, input().split()) # V개의 노드 개수와 방향성이 없는 E개의 간선 정보
    edge = [list(map(int, input().split())) for i in range(E)]  # 간선의 양쪽 노드 번호
    start, goal = map(int, input().split()) # 출발 노드, 도착 노드
    G = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for i in range(E):
        n1, n2 = edge[i][0], edge[i][1]
        G[n1].append(n2) # 방향이 없기 때문에
        G[n2].append(n1) # 방향이 없기 때문에

    BFS(t, start, goal)