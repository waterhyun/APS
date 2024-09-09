# 톱니 바퀴

import sys
sys.stdin = open('boj/input.txt', 'r')

def discriminant(cogwheels, wheel_num):
    sn_state = [True] * 3
    for idx in range(3):
        if cogwheels[idx][2] != cogwheels[idx+1][6]:
            sn_state[idx] = False

    sn_state.insert(wheel_num, False)
    return sn_state

def rotate(wheel_num, direction):
    global cogwheels
    temp = cogwheels[wheel_num]
    print(f'{wheel_num}번 톱니바퀴, 전: {temp}')
    if direction == 1:
        cogwheels[wheel_num] = [temp[-1]] + temp[:-1]
        print(f'{wheel_num}번 톱니바퀴, 후 {cogwheels[wheel_num]}')
    else:
        cogwheels[wheel_num] = temp[1:] + [temp[0]]
        print(f'{wheel_num}번 톱니바퀴, 후 {cogwheels[wheel_num]}')

def func(wheel_num, direction):
    global cogwheels
    print(f'함수 실행 {wheel_num}')
    rotate(wheel_num, direction)

    # 왼쪽
    if 0 <= wheel_num-1 < 4 and not sn_state[wheel_num-1]:
        print(f'현재 {wheel_num}, 다음 {wheel_num-1}')
        func(wheel_num-1, -direction)
    # 오른쪽 
    if 0 <= wheel_num + 1 < 4 and not sn_state[wheel_num+1]:
        print(f'현재 {wheel_num}, 다음 {wheel_num+1}')
        func(wheel_num+1, -direction)

def score_func(cogwheels):
    score = 0
    for i in range(4):
        state = cogwheels[i][0]
        if state == 1:
            score += 2**i
    return score


cogwheels = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())
rotation_plan = [list(map(int, input().split())) for _ in range(K)]
for wheel_num, direction in rotation_plan:
    for i in range(4):
        print(cogwheels[i])
    wheel_num -= 1
    sn_state = discriminant(cogwheels, wheel_num)
    print(sn_state)
    func(wheel_num, direction)
    print('---')

result = score_func(cogwheels)
print(result)