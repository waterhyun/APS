# 오목 판정 D3

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    flag = False
    for i in range(n):
        row_cnt = 0
        col_cnt = 0
        for j in range(n):
            if arr[i][j] == 'o':
                row_cnt += 1
                if row_cnt >= 5:
                    flag = True
                    break
            else:
                row_cnt = 0

            if arr[j][i] == 'o':
                col_cnt += 1
                if col_cnt >= 5:
                    flag = True
                    break
            else:
                col_cnt = 0

    if not flag:
        for i in range(n):
            for j in range(n):
                if i <= n - 5 and j <= n - 5:
                    count = 0
                    for k in range(5):
                        if arr[i + k][j + k] == 'o':
                            count += 1
                        else:
                            break

                    if count == 5:
                        flag = True
                        break

                if i >= 4 and j <= n - 5:
                    count = 0
                    for k in range(5):
                        if arr[i - k][j + k] == 'o':
                            count += 1
                        else:
                            break
                    if count == 5:
                        flag = True
                        break
            if flag:
                break
    if flag:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')

###############################

di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

def f(n):
    for i in range(n):
        for j in range(n):
            for k in range(4):
                cnt = 0
                ni, nj = i, j
                while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'                    
                    ni += di[k]
                    nj += dj[k]    
    return 'NO'

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    ans = f(n)
    print(f'#{t} {ans}')