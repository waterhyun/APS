# 20397. 돌 뒤집기 게임 2

tc = int(input())
for t in range(1, tc+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    play = [list(map(int, input().split())) for _ in range(M)]

    for i, j in play:
        i -= 1
        for k in range(1, j+1):
            if i - k >= 0 and i + k < N :
                if arr[i-k] == arr[i+k] and arr[i-k] == 1:
                    arr[i-k] = arr[i+k] = 0
                elif arr[i-k] == arr[i+k] and arr[i-k] == 0:
                    arr[i-k] = arr[i+k] = 1
            else:
                break
        

    print(f'#{t}', *arr)

