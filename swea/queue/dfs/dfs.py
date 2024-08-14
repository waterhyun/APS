'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

#############################################
# 탐색순서 

def bfs(s, V): # 시작점s, 마지막 정점 v
    # 준비
    visited = [0] * (V+1)
    q = []
    q.append(s)
    visited[s] = 1
    # 탐색
    while q:
        t = q.pop(0)
        print(t, end= ' ')
        for w in adj_l[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1


V, E = map(int, input().split()) # V는 마지막 번호, E 간선 수
arr = list(map(int, input().split()))
adj_l = [[] for _ in range(V+1)] # 인접 리스트

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1) # 방향이 없으면

bfs(1, V) # 출발점, 정점수

#####################################################################
# 엣지 개수

def bfs(s, V): # 시작점s, 마지막 정점 v
    # 준비
    visited = [0] * (V+1)
    q = []
    q.append(s)
    visited[s] = 1
    # 탐색
    while q:
        t = q.pop(0)
        for w in adj_l[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

    print(visited) # 간선 개수 확인 가능

V, E = map(int, input().split()) # V는 마지막 번호, E 간선 수
arr = list(map(int, input().split()))
adj_l = [[] for _ in range(V+1)] # 인접 리스트

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1) # 방향이 없으면

bfs(1, V) # 출발점, 정점수