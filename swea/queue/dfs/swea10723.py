# 5105. [기본] 6일차 - 미로의 거리 (제출용) D3

# 2에서 출발해서 # 3까지 가기
# 1은 벽 # 0은 통로


tc = int(input())   # 테스트 케이스
for T in range(1, tc+1):
    n = int(input())    # 미로의 크기
    maze = [list(map(int, input().strip())) for _ in range(n)]  # 한 줄씩 숫자로 변환하여 리스트에 저장
    visited = [[0] * n for _ in range(n)]


    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                positions = [i, j]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue = []
    queue.append((positions[0], positions[1]))
    visited[positions[0]][positions[1]] = 1
    flag = False
    while queue:
        t = queue.pop(0)
        if maze[t[0]][t[1]] == 3:
            flag = True
            print(f'#{T} {visited[t[0]][t[1]]-2}')
        for d in range(4):
            ni = t[0] + dx[d]
            nj = t[1] + dy[d]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                queue.append((ni, nj))
                visited[ni][nj] = visited[t[0]][t[1]] + 1

    if not flag:
        print(f'#{T} 0')





