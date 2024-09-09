# 마법사 상어와 토네이도
import sys
sys.stdin = open('boj/input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

nx = N//2
ny = N//2

left = [(-1, 1, 0.01), 
        (1, 1, 0.01),
        (-2, 0, 0.02), 
        (2, 0, 0.02),
        (-1, 0, 0.07), 
        (1, 0, 0.07),
        (-1, -1, 0.1), 
        (1, -1, 0.1),
        (0, -2, 0.05), 
        (0, -1, 0)] 
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, -x, z) for x, y, z in left]

direction = {'left': left,
             'right': right,
             'down': down,
             'up': up}

def tornado(arr, dx, dy, step, direct):
    global nx, ny, disappear_amount

    if nx == -1 or ny == -1:
        return

    for _ in range(step):
        nx += dx
        ny += dy

        if 0 <= nx < N and 0 <= ny < N:
            # y의 위치
            dust = arr[nx][ny]
            use_amount = 0
            if dust != 0:
                for x, y, z in direction[direct]:
                    temp_x = nx + x
                    temp_y = ny + y
                    dust_amount = int(dust * z)
                    if 0 <= temp_x < N and 0 <= temp_y < N:
                        if z == 0:
                            arr[temp_x][temp_y] += (dust - use_amount)
                        else:
                            arr[temp_x][temp_y] += dust_amount
                            use_amount += dust_amount
                    else:
                        if z == 0:
                            disappear_amount += (dust - use_amount)
                        else:
                            use_amount += dust_amount
                            disappear_amount += dust_amount

                arr[nx][ny] = 0

disappear_amount = 0
for i in range(N):
    step = (2 * i) + 1
    # 왼쪽
    tornado(arr, 0, -1, step, 'left')
    # 아래
    tornado(arr, 1, 0, step, 'down')
    step = (2 * i) + 2
    # 오른쪽
    tornado(arr, 0, 1, step, 'right')
    # 위쪽
    tornado(arr, -1, 0, step, 'up')

print(disappear_amount)
