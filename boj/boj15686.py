# 치킨 배달
# 백트래킹으로 풀어보기

import sys
from itertools import combinations

def chicken_to_house(chicken_location, house_location):
    result = 0
    for hx, hy in house_location:
        min_v = float('inf')
        for cx, cy in chicken_location:
            value = abs(hx - cx) + abs(hy - cy)
            if min_v > value:
                min_v = value
        result += min_v
    return result
     

def backtracking(chicken_location, house_location, M):
    min_v = float('inf')
    for cc in combinations(chicken_location, M):
        value = chicken_to_house(cc, house_location)
        if value < min_v:
            min_v = value
    
    return min_v


N, M = map(int, input().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken_location = list() # 치킨 집 정보
house_location = list() # 집 정보

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:  # 1은 집, 2는 치킨집
            chicken_location.append((i, j))
        elif city[i][j] == 1:
            house_location.append((i, j))

result = backtracking(chicken_location, house_location, M)
print(result)