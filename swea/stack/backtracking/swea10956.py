import sys
sys.stdin = open('swea\input.txt', 'r')


# 충전지가 방전되기 전에 교체하며 운행해야 하는데
# 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야함

# 재귀 함수 정의
def func(now_position):
    global min_charge
    # 종료조건
    if now_position >= N-1:
        if min_charge > len(used) - 1:
            min_charge = len(used) - 1
        return
    # 유효성 검사
    step = arr[now_position]
    used.append(step)
    for s in range(1, step+1):
        # 백트래킹
        if len(used)-1 < min_charge:
            func(now_position + s)
    used.pop()


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split())) # 충
    N = arr.pop(0) # 정류장 수

    # 상태 표현
    used = list() 
    min_charge = float('inf')
    func(0)

    print(f'#{tc} {min_charge}')