import sys
sys.stdin = open('swea/input.txt', 'r')

from collections import deque

def cal_f(n, m):
    queue = deque([(n, 0)])
    visited = set([n])

    while queue:
        num, ops = queue.popleft()
        if num == m:
            return ops
        
        for next_num in (num+1, num-1, num*2, num-10):
            if 1 <= next_num <= 1000000 and next_num not in visited:
                queue.append([next_num, ops+1])
                visited.add(next_num)
    
    return -1



T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    result = cal_f(n, m)
    print(f'#{tc} {result}')

