# 10014. 5248. 그룹 나누기(제출용)
import sys
sys.stdin = open('swea/input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # jo = [0] * (N + 1)d
    # arr = list(map(int, input().split()))
    # for a in arr:
    #     jo[a] += 1
    
    # cnt = 0
    # for a in arr:
    #     if jo[a] >= 1:
    #         cnt += 1

    # print(f'#{tc} {cnt}')