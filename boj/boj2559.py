# 수열

############ Slicing Window
import sys
n, k = map(int, sys.stdin.readline().split()) # 전체 날짜 수, 합을 구하기 위한 연속적인 날짜
numbers = list(map(int, sys.stdin.readline().split()))

window = sum(numbers[:k])
result = window

for i in range(k, n):
    window += numbers[i] - numbers[i-k]
    result = max(result, window)

print(result)

############ 시간 초과
n, k = map(int, input().split()) # 전체 날짜 수, 합을 구하기 위한 연속적인 날짜
numbers = list(map(int, input().split()))
sum_list = [0] * (n-k+1)
for i in range(n-k+1):
    total = 0
    for j in range(i, i+k):
        total += numbers[j]
    sum_list[i] = total

result = sum_list[0]
for value in sum_list:
    if result < value:
        result = value

print(result)


