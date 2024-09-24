# 10017. 5249. 최소 신장 트리 (제출용)
import sys
sys.stdin = open('swea/input.txt', 'r')

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())
for tc in range(1, T+1):
    # 입력 받기
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        a, b, w = map(int, input().split())
        edges.append((w, a, b))

    # 간선을 가중치 기준으로 정렬
    edges.sort()

    # 각 노드의 부모를 자기 자신으로 초기화
    parent = list(range(V + 1))

    total_weight = 0
    cnt = 0

    for weight, n1, n2 in edges:
        if find_set(n1) != find_set(n2):  # 사이클이 없다면
            # print(weight, n1, n2)
            union(n1, n2) # 합치기
            total_weight += weight
            cnt += 1
            if cnt == V:  # V개의 간선을 선택하면 종료
                break

    print(f'#{tc} {total_weight}')
