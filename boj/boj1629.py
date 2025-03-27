import sys
sys.stdin = open('boj/input.txt', 'r')
A, B, C = map(int, input().split())

def cal(A, B):
    print(A, B)
    if B == 1:
        return A % C
    half = cal(A, B // 2)
    if B % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * A) % C

print(cal(A, B))
