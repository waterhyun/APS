# 4875. [기본] 5일차 - 미로 (제출용) D3

##### 첫 번째 답안 - 재귀 - 메모리, 시간 측면에서 많이 나옴
def dfs(i, j, n):
    visited[i][j] = 1
    if maze[i][j] == 3: # 도착
        return 1
    else:
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                if dfs(ni, nj, n):
                    return 1
        return 0
 
# 방문한 칸을 표시하기
def fstart(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j
    return -1, -1  # 디버깅 목적
 
# 테스트 케이스
tc = int(input())
for t in range(1, tc+1):
    n = int(input()) # 미로 크기 입력
    maze = [list(map(int, input())) for _ in range(n)] # 미로 입력
 
    # 출발점 찾기
    sti, stj = fstart(n)
 
    visited = [[0]*n for _ in range(n)] # dfs용
    print(f'#{t} {dfs(sti, stj, n)}')




##### 두 번째 답안 - 스택 - 첫 번째 답안 보다 좋게 나옴

def dfs_stack(i, j, N):
    # 지금 위치는 방문했으니깐 1로 처리
    stack = [(i, j)]
    visited[i][j] = 1 
    while stack:
        now_i, now_j = stack.pop() # 
 
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = now_i+di, now_j+dj
            # 주변에 통로가 있나용?
            # 네!
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                # 도착지
                if maze[ni][nj] == 3:
                    return True
                # 도착지가 아니면
                stack.append((ni, nj))
                visited[ni][nj] = 1 # 왔던 길로 처리
            # 주변에 통로 없으면 pop = 뒤로가기 2로 돌아갔는데도 없으면 False로
    return False
 
 
# 방문한 칸을 표시하기
def fstart(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j
    return -1, -1  # 디버깅 목적
 
# 테스트 케이스
tc = int(input())
for t in range(1, tc+1):
    n = int(input()) # 미로 크기 입력
    maze = [list(map(int, input())) for _ in range(n)] # 미로 입력
 
    # 출발점 찾기
    sti, stj = fstart(n)
 
    visited = [[0]*n for _ in range(n)]
    if dfs_stack(sti, stj, n):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')