# 4881. [기본] 5일차 - 배열 최소 합 D3


def f(row, V, arr, bit, visited_col, now_sum):
    global min_value
    if row == V:
        if now_sum < min_value:
            min_value = now_sum
        return # row == V이므로 해당 함수가 끝남
    for col in range(V):
        if not visited_col[col]:  # 방문한 적이 없다면
            bit[row][col] = 1  # 방문
            visited_col[col] = True
            new_sum = now_sum + arr[row][col]  # 방문한 곳의 값을 넣기
            f(row+1, V, arr, bit, visited_col, new_sum)  # 재귀로 다음 행으로 넘어감
            bit[row][col] = 0
            visited_col[col] = False
 
tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bit = [[0] * N for _ in range(N)]
    visited_col = [False]*N
    min_value = float('inf')
    f(0, N, arr, bit, visited_col, 0)
    print(f'#{t} {min_value}')