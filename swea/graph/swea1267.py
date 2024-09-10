# 10일차 - 작업순서
import sys
sys.stdin = open('swea/input.txt', 'r')

from collections import deque

def f(V):  # 위상 정렬
    # 큐 생성
    queue = deque()
    
    # visited 생성
    visited = [0] * (V+1)
    
    # 진입차수가 0인 정점 인큐
    for i in range(1, V+1):
        if ind[i] == 0:
            # 인큐
            queue.append(i)
            # 인큐된 정점 visited 표시
            visited[i] = 1

    # ---------------------------- 준비 작업

    while queue:
        # 처리된 순서이기 때문에
        t = queue.popleft()

        # 8, 4나 둘다 먼저 처리되어도 상관 없는데
        # 4를 먼저 처리해달라고 하면 다시 어떤 정렬을 해줘야 함
        # 규칙에만 맞으면 출력하면 됨
        print(t, end = ' ') # visited(t)
        
        # t에 인접한 i의 진입차수 하나 감소, 0일 때 enqueue
        for i in adj[t]:
            # 처리 되었다는 뜻 (-> ind[i] == 0 인큐 조건)
            ind[i] -= 1
            if ind[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1 # 전체 걸린 시간을 계산해야한다면 필요한 정보이기 때문에 해줌

    print()

for tc in range(1, 11):
    # 정점의 개수 V(3 ≤ V ≤ 1000)
    # 간선의 개수 E(2 ≤ E ≤ 3000)
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    # 진입 차수, 인접리스트(혹은 인접 행렬)
    ind = [0] * (V+1)
    adj = [[] for _ in range(V+1)]
    for i in range(E):
        # n1 출발, n2도착
        n1, n2 = arr[i*2], arr[i*2+1] 
        
        adj[n1].append(n2)  # 방향 그래프
        # adj[n2].append(n1) # 무방향 그래프 -> 테케는 맞도록 속일 수 있음
        ind[n2] += 1        # 진입차수(도착으로 언급된 횟수)

    print(f'#{tc}', end = ' ')
    f(V)
    # print()