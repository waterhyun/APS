# 16811. 당근 포장하기

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    min_v = 30000
    for i in range(N-2):
        for j in range(i+1, N-1):
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                a = i + 1  # 소 상자 당근 개수
                b = j - i  # 중 상자 당근 개수
                c = N - 1 - j  # 대 상자 당근 개수
                if a <= N//2 and b <= N//2 and c <= N//2:
                    if min_v > max(a, b, c) - min(a, b, c):
                        min_v = max(a, b, c) - min(a, b, c)
        
    if min_v == 30000:
        min_v = -1
    print(f'#{t} {min_v}')
