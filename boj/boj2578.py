# 빙고
arr = [list(map(int, input().split())) for _ in range(5)]
numbers = []
for _ in range(5):
    numbers += list(map(int, input().split()))

# 행, 열, 대각선 카운트
row_cnt = [0] * 5
col_cnt = [0] * 5
x1_cnt = 0
x2_cnt = 0
result = 0

# 완료된 행과 열을 추적
completed_rows = set()
completed_cols = set()

for ind, n in enumerate(numbers):
    # 숫자의 위치를 찾아서 마킹
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                row_cnt[i] += 1
                col_cnt[j] += 1
                if i == j:
                    x1_cnt += 1
                if i == (4-j):
                    x2_cnt += 1
                
                # 완료된 줄을 체크
                if row_cnt[i] == 5 and i not in completed_rows:
                    result += 1
                    completed_rows.add(i)
                if col_cnt[j] == 5 and j not in completed_cols:
                    result += 1
                    completed_cols.add(j)
                if x1_cnt == 5 and 'x1' not in completed_rows:
                    result += 1
                    completed_rows.add('x1')
                if x2_cnt == 5 and 'x2' not in completed_rows:
                    result += 1
                    completed_rows.add('x2')
                
                if result >= 3:
                    print(ind+1)
                    break
        else:
            continue
        break
    else:
        continue
    break


'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''

###############################

# arr = [list(map(int, input().split())) for _ in range(5)]
# numbers = []
# for _ in range(5):
#     numbers += list(map(int, input().split()))

# ind = 0
# row_cnt = [0] * 5
# col_cnt = [0] * 5
# x1_cnt = 0
# x2_cnt = 0
# result = 0
# for n in numbers:
#     for i in range(5):
#         for j in range(5):
#             if arr[i][j] == n:
#                 ind += 1
#                 row_cnt[i] += 1
#                 col_cnt[j] += 1
#                 if i == j:
#                     x1_cnt += 1
#                 if i == (4-j):
#                     x2_cnt += 1
#                 print(f'ind:{ind}, n:{n}, i:{i}, j:{j}, row_cnt:{row_cnt[i]}, '
#                       f'col_cnt:{col_cnt[j]}, x1_cnt:{x1_cnt}, x2_cnt:{x2_cnt}')
#                 if row_cnt[i] == 5 or col_cnt[j] == 5 or x1_cnt == 5 or x2_cnt == 5:
#                     # 한번 x2_cnt가 5가 되면 계속 플러스가 된다는 단점이 있음 ㅠㅠ
#                     if row_cnt[i] == 5:
#                         result += 1
#                     if col_cnt[j] == 5:
#                         result += 1
#                     if x1_cnt == 5:
#                         result += 1
#                     if x2_cnt == 5:
#                         result += 1
#                     print('####', result)
#                     if result >= 3:
#                         print('@@@@@@@@@@@@@@@@@', ind)
#                         break
#                 continue