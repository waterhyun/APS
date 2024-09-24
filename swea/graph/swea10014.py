# 10014. 5248. 그룹 나누기(제출용)
import sys
sys.stdin = open('swea/input.txt', 'r')

# 원소가 속한 집합의 대표 원소 찾기
def find(parent, x):
    if parent[x] != x:
        # 압축 작업
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 개의 집합을 합쳐서 하나의 집합으로 만들기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())
for tc in range(1, T+1):

    # 학생수, 신청서 수
    n, m = map(int, input().split())

    parent = list(range(n+1)) # 초기화, 0번 인덱스는 사용하지 않음

    # 신청서 부분 처리하기
    application = list(map(int, input().split()))
    for i in range(0, len(application), 2):
        a, b = application[i], application[i+1]
        union(parent, a, b)

    # 그룹 수 계산
    groups = set()
    for i in range(1, n+1):
        groups.add(find(parent, i))

    print(f'#{tc} {len(groups)}')
