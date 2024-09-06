# 5209. 최소생산비용

import sys
sys.stdin = open('swea\input.txt', 'r')
def backtracking(factory, current_cost):
    global min_cost
    if factory == N:
        # 모든 공장에 상품이 할당되었으면 총 비용 계산
        if current_cost < min_cost:
            min_cost = current_cost
        return

    # 상품 0, 1, 2를 봄
    for product in range(N):
        # 이미 본 상품이라면 패스
        if product not in lst:
            lst[factory] = product  # 공장 - 상품 매칭
            # 현재 비용과 새로운 비용을 비교
            new_cost = current_cost + arr[factory][product]
            if new_cost < min_cost:
                backtracking(factory + 1, new_cost)  # 다음 공장 탐색
            lst[factory] = -1  # 안 본 것으로 다시 보기

    return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [-1] * N
    min_cost = float('inf')
    backtracking(0, 0)
    print(f'#{tc} {min_cost}')
