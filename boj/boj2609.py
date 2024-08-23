
a, b = map(int, input().split())
max_v = 1  # 기본값으로 초기화
for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        max_v = i
print(max_v)
print((a // max_v) * b)
