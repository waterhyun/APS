import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    N = int(N)
    result = ''.join(bin(int(n, 16))[2:].zfill(4) for n in num)
    print(f'#{tc} {result}')
