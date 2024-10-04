# 테트로미노
import sys
sys.stdin = open('boj/input.txt', 'r')
# from itertools import combinations
# from collections import deque
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

def get_sum(x, y, tetromino):
    total = 0
    for dx, dy in tetromino:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            total += grid[nx][ny]
        else:
            return 0
    return total

# 테트로미노 모양 수정
tetrominos = [
    [(0,0), (0,1), (0,2), (0,3)],  # ㅡ
    [(0,0), (1,0), (2,0), (3,0)],  # ㅣ
    [(0,0), (0,1), (1,0), (1,1)],  # ㅁ
    [(0,0), (1,0), (2,0), (2,1)],  # ㄴ
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,1), (1,1), (2,1), (2,0)],
    [(0,0), (0,1), (0,2), (1,2)],  # ㄱ
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (1,0), (2,0), (0,1)],
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)],  # ㄹ
    [(1,0), (1,1), (0,1), (0,2)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(0,1), (1,0), (1,1), (2,0)],
    [(0,0), (0,1), (0,2), (1,1)],  # ㅜ
    [(0,1), (1,0), (1,1), (1,2)],
    [(0,0), (1,0), (1,1), (2,0)],
    [(1,0), (0,1), (1,1), (2,1)]
]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0
for i in range(N):
    for j in range(M):
        for tetromino in tetrominos:
            max_sum = max(max_sum, get_sum(i, j, tetromino))

print(max_sum)


# grid_ij = [(i, j) for i in range(N) for j in range(M)]
# temp = list(combinations(grid_ij, 4))
# combinations_list = []
# for i in range(len(temp)):
#     comb = list(temp[i])
#     # print(comb)
#     flag = True
#     all_c = 0
#     for c in comb:
#         count_c = 0 
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
#             ni, nj = c
#             ni += di
#             nj += dj
#             if 0 <= ni < N and 0 <= nj < M and (ni, nj) in comb:
#                 count_c += 1
#         if count_c >= 2:
#             all_c += 1

#     if all_c == 4:
#         # print('Yes')
#         combinations_list.append(comb)

# result = 0
# for comb in combinations_list:
#     # print(comb)
#     value = 0
#     for i, j in comb:
#         value += grid[i][j]
#     if result < value:
#         print(value, comb)
#     # print(value, comb)
#     result = max(value, result)
# print(result)
               