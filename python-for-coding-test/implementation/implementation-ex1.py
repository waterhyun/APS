# 상하좌우

n  = int(input()) # 공간의 크기
plans = list(input().split()) # 이동 계획서

# 오른쪽, 왼쪽, 아래, 위
dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0]
move_types = {'R':0, 'L':1, 'D':2, 'U':3}

start = [1, 1]

for i in range(len(plans)):
    d = move_types[plans[i]]
    if 0 < start[0] + dx[d] < (n+1) and 0 < start[1] + dy[d] < (n+1) :
        start[0] += dx[d]
        start[1] += dy[d]
        
print(*start)
