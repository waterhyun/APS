# 1979. 어디에 단어가 들어갈 수 있을까

tc = int(input())
for t in range(1, tc+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split()))+[0] for _ in range(n)] + [[0] * (n+1)]

    row_cnt_lst = []
    col_cnt_lst = []
    total = 0

    for i in range(n+1):
        row_cnt = 0
        for j in range(n+1):
            if arr[i][j] == 1:
                row_cnt += 1
            elif row_cnt > 0 and arr[i][j] == 0:
                row_cnt_lst.append(row_cnt)
                row_cnt = 0

    for i in range(n+1):
        col_cnt = 0
        for j in range(n+1):
            if arr[j][i] == 1:
                col_cnt += 1
            elif col_cnt > 0 and arr[j][i] == 0:
                col_cnt_lst.append(col_cnt)
                col_cnt = 0

    total += row_cnt_lst.count(k)
    total += col_cnt_lst.count(k)

    print(f'#{t} {total}')

###################################################################

tc = int(input())
for t in range(1, tc+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    total = 0

    # 행과 열에서 k개의 1이 연속으로 나오는지 체크하는 함수
    def count_k_in_line(line):
        count = 0
        result = 0
        for value in line + [0]:  # 배열 끝에 0을 추가해 마지막 연속 1의 처리를 용이하게 함
            if value == 1:
                count += 1
            else:
                if count == k:
                    result += 1
                count = 0
        return result

    # 행 체크
    for i in range(n):
        total += count_k_in_line(arr[i])

    # 열 체크
    for j in range(n):
        total += count_k_in_line([arr[i][j] for i in range(n)])

    print(f'#{t} {total}')
