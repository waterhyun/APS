# 숨바꼭질 4

# 걷기 x-1, x+1
# 순간이동 2*x

import heapq

N, K = map(int, input().split())
INF = int(1e9)
distance = [INF] * (100001)  # 최단 거리 저장
prev = [-1] * (100001)  # 이전 노드 저장

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        time, now = heapq.heappop(q)

        if distance[now] < time:
            continue
        
        if now == K:
            return time

        for next_node in (now - 1, now + 1, now * 2):
            if 0 <= next_node <= 100000 and distance[next_node] > time + 1:
                distance[next_node] = time + 1
                prev[next_node] = now  # 이동 경로 저장
                heapq.heappush(q, (time + 1, next_node))

    return -1

# 최단 시간 찾기
time = dijkstra(N)

# 경로 추적
path = []
cur = K
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()  # 역순이므로 뒤집기

# 출력
print(time)
print(' '.join(map(str, path)))

