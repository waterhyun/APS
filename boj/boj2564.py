
# width, height, store_num <= 100 자연수  
width, height = map(int, input().split())  # 가로, 세로 길이
store_num = int(input())  # 상점 개수

# 상점 위치 받기
stores = [list(map(int, input().split())) for _ in range(store_num)]
# stores[0][0] - 상점이 위치한 방향
# 1 - 북
# 2 - 남
# 3 - 서
# 4 - 동
# stores[0][1]
# 상점이 블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리
# 상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리

# 동근이 위치
d, x = map(int, input().split())

