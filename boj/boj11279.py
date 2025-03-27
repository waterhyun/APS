# 최대 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if not arr:
            print(0)
        else:
            pop = heapq.heappop(arr)
            print(-pop)
    else:
        heapq.heappush(arr, -x)
