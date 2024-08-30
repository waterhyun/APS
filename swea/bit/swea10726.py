# 10726. 이진수 표현

# 정수 N, M 이 주어질 때, 
# M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력하라.
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    if m & ((1<<n)-1) == ((1<<n)-1):
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')
