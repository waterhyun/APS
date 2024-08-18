# 11039. 사각형 찾기
# 크기가 NxN인 2차원 배열 내부에 1로 채워진 사각 영역이 있다. 
# 사각형의 가로 세로 칸수를 곱한 값을 출력하는 프로그램을 만드시오. 
# 사각형이 여러 개인 경우 곱이 가장 큰 경우를 출력한다.

# 왼쪽 위 모서리 찾기
def f(arr, x, y):
    # 해당 칸이 1인가요?
    if arr[x][y] != 1:
        return False
    # 위
    if x > 0 and arr[x-1][y] != 0:
        return False
    # 왼쪽
    if y > 0 and arr[x][y-1] != 0:
        return False
    return True
            
tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(N):
        for j in range(N):
            if f(arr, i, j):
                width, height = 0, 0

                for k in range(j, N):
                    if arr[i][k] == 1:
                        width += 1
                    else:
                        break
                
                for k in range(i, N):
                    if arr[k][j] == 1:
                        height += 1
                    else:
                        break
                
                value = width * height
                if value > max_value:
                    max_value = value

    print(f'#{t}', max_value)


        