# 20739. 고대 유적 2

tc = int(input())  # 테스트 케이스의 개수
for t in range(1, tc + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    max_v = 0
 
    for i in range(N):
        row_v = 0
        for j in range(M):
            if arr[i][j] == 1:
                row_v += 1
            else:
                if row_v >= 2:
                    max_v = max(max_v, row_v)
                row_v = 0
        # 마지막 부분 처리
        if row_v >= 2:
            max_v = max(max_v, row_v)
 
    for i in range(M):
        col_v = 0
        for j in range(N):
            if arr[j][i] == 1:
                col_v += 1
            else:
                if col_v >= 2:
                    max_v = max(max_v, col_v)
                col_v = 0
        # 마지막 부분 처리
        if col_v >= 2:
            max_v = max(max_v, col_v)
 
    # 결과 출력
    print(f'#{t} {max_v}')
