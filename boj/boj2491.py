# 수열, 실버 4
def sizing(n, numbers):
    if n == 1:
        return 1
    
    rcnt = 1  # 증가 구간 카운트
    lcnt = 1  # 감소 구간 카운트
    max_size = 1  # 최대 길이
    
    for idx in range(1, n):
        if numbers[idx] >= numbers[idx - 1]:
            rcnt += 1
        else:
            rcnt = 1
        if numbers[idx - 1] >= numbers[idx]:
            lcnt += 1
        else:
            lcnt = 1
        print(f'numbers:{numbers[idx]}, rcnt: {rcnt}, lcnt: {lcnt}')
        
        max_size = max(max_size, rcnt, lcnt)
    
    return max_size

n = int(input())
numbers = list(map(int, input().split()))

print(sizing(n, numbers))



# n = int(input())
# numbers = list(map(int, input().split()))
# rcnt = 0
# lcnt = 0
# max_size = 0
# for idx in range(n-1):
#     if numbers[idx] <= numbers[idx + 1]:
#         rcnt += 1
#         print(idx, numbers[idx], rcnt)
#     else:
#         rcnt += 1
#         max_size = max(rcnt, lcnt, max_size)
#         print('#', idx, numbers[idx], rcnt)
#         rcnt = 0
#     if numbers[idx] >= numbers[idx + 1] :
#         print(idx, numbers[idx], lcnt)
#         lcnt += 1
#     else:
#         lcnt += 1
#         max_size = max(rcnt, lcnt, max_size)
#         print('#', idx, numbers[idx], lcnt)
#         lcnt = 0
#     print('---------------')
#     max_size = max(rcnt, lcnt, max_size)

# print(max_size)