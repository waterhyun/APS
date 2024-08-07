# 수 이어가기, 실버 5

# 첫 줄
num = int(input()) # 1 <= num <= 30000
max_size = 1
for i in range(1, num+1):
    arr = [num]
    arr.append(i)
    idx = 1
    while True:
        value = arr[idx-1] - arr[idx]
        if value < 0:
            if max_size < len(arr):
                max_size = len(arr)
                result_arr = arr
                break
            break
        else:
            arr.append(value)
            idx += 1

print(max_size)
print(*result_arr)
