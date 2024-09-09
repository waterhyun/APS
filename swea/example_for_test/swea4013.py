import sys
sys.stdin = open('swea/input.txt', 'r')

def rotate(wheel, direction):
    return wheel[-direction:] + wheel[:-direction]

def score_func(cogwheels):
    return sum(wheel[0] << i for i, wheel in enumerate(cogwheels))

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    cogwheels = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        wheel_num, direction = map(int, input().split())
        wheel_num -= 1

        rotations = [0] * 4
        rotations[wheel_num] = direction

        # 왼쪽 확인
        for i in range(wheel_num - 1, -1, -1):
            if cogwheels[i][2] != cogwheels[i+1][6]:
                rotations[i] = -rotations[i+1]
            else:
                break

        # 오른쪽 확인
        for i in range(wheel_num + 1, 4):
            if cogwheels[i-1][2] != cogwheels[i][6]:
                rotations[i] = -rotations[i-1]
            else:
                break

        # 회전 적용
        cogwheels = [rotate(wheel, r) for wheel, r in zip(cogwheels, rotations)]

    print(f'#{tc} {score_func(cogwheels)}')
