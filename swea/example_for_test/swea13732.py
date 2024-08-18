# 13732. 정사각형 판정
def f(grid, min_x, min_y, length, N):
    # 정사각형 범위가 유효한지 검사
    if min_x + length > N or min_y + length > N:
        return False
    
    for i in range(min_x, min_x + length):
        for j in range(min_y, min_y + length):
            if grid[i][j] != '#':
                return False
    
    return True


tc = int(input())
for t in range(1, tc + 1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    
    min_x = N
    max_x = -1
    min_y = N
    max_y = -1

    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#':
                if i < min_x:
                    min_x = i
                if i > max_x:
                    max_x = i
                if j < min_y:
                    min_y = j
                if j > max_y:
                    max_y = j

    length_x = max_x - min_x + 1
    length_y = max_y - min_y + 1
    if length_x != length_y:
        print(f'#{t} no')
    else:
        length = max_x - min_x + 1
        if f(grid, min_x, min_y, length, N):
            print(f'#{t} yes')
        else:
            print(f'#{t} no')
