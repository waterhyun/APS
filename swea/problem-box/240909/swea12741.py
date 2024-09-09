# 두 전구
import sys
sys.stdin = open('swea/input.txt', 'r')

T = int(input())
results = []
for tc in range(1, T+1):
    a, b, c, d = map(int, input().split())
    start = max(a, c)
    end = min(b, d)
    if start - end >= 0:
        results.append(0)
    else:
        results.append(end-start)

for tc, result in enumerate(results):
    print(f'#{tc+1} {result}')
