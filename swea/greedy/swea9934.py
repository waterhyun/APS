import sys
sys.stdin = open('swea\input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수
    arr_w = list(map(int, input().split()))  # 화물의 무게
    arr_t = list(map(int, input().split()))  # 적재 용량

    # 트럭 당 한 개의 컨테이너 운반
    used = [False] * N
    # 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없음
    # 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮김
    # 옮겨진 화물의 전체 무게가 얼마인가!

    arr_w.sort(reverse=True)
    arr_t.sort(reverse=True)

    total = 0
    for truck in arr_t:
        optimal_weight = 0
        for idx, weight in enumerate(arr_w):
            if truck >= weight and not used[idx]:
                if optimal_weight <= weight:
                    optimal_idx = idx
                    optimal_weight = weight
        
        if optimal_weight != 0:
            used[optimal_idx] = True
            total += optimal_weight

    print(f'#{tc} {total}')