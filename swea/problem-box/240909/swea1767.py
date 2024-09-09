import sys
sys.stdin = open('swea/input.txt', 'r')

def dfs(index, connected, length):
    global max_connected, min_length
    
    # 종료 조건
    if index == len(cores):
        # 가장 많이 연결한 상태에서, 길이의 최소값을 구함
        if connected > max_connected:
            max_connected = connected
            min_length = length
        elif connected == max_connected:
            min_length = min(min_length, length)
        return

    # 코어의 위치를 거내서
    x, y = cores[index]
    # 설치 가능한지 체크
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        # 해당 위치에서 직선을 만들 수 있다면
        if can_connect(x, y, dx, dy):
            # 연결 (전선(2)를 깔면서 길이 계산)
            line_length = connect(x, y, dx, dy)
            # 다음 코어를 확인해봄
            dfs(index + 1, connected + 1, length + line_length)
            disconnect(x, y, dx, dy)  # 초기화 작업

    dfs(index + 1, connected, length)

def can_connect(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    # 범위를 넘지 않는 선에서
    while 0 <= nx < N and 0 <= ny < N:
        # 직선을 만들다가, 빈셀이 아닌 구간(즉 다른 셀이 있을 때) 끝
        if maxinox[nx][ny] != 0:
            return False
        # 계속 더하며 직선을 만듦
        nx += dx
        ny += dy

    # 끝까지 만들 수 있다면 True
    return True


def connect(x, y, dx, dy):
    # 길이를 구해봄
    length = 0
    nx, ny = x + dx, y + dy
    while 0 <= nx < N and 0 <= ny < N:
        maxinox[nx][ny] = 2  # 2는 전선을 의미
        length += 1
        nx += dx
        ny += dy
    return length

def disconnect(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    while 0 <= nx < N and 0 <= ny < N:
        # 전선 지우기
        maxinox[nx][ny] = 0
        nx += dx
        ny += dy


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maxinox = [list(map(int, input().split())) for _ in range(N)]
    
    # 코어의 위치
    cores = [(i,j) for i in range(1, N-1) for j in range(1, N-1) if maxinox[i][j] == 1]

    # 최대한 많은 core에 전원 연결을 하였을 경우, 전선 길이의 합 최소
    # 최대한 많은 core 연결 => max_connected
    # 전선 길이의 합 최소 => min_length
    # 우선순위 : max_connected > min_length
    max_connected = 0
    min_length = 1e9

    dfs(0, 0, 0)

    print(f'#{test_case} {min_length}')

