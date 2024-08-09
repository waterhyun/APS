# 직사각형

def intersection_type(x1, y1, p1, q1, x2, y2, p2, q2):
    # 교차 부분의 좌표를 계산합니다.
    ix1 = max(x1, x2)
    iy1 = max(y1, y2)
    ix2 = min(p1, p2)
    iy2 = min(q1, q2)

    # 교차 부분의 너비와 높이를 계산합니다.
    width = ix2 - ix1
    height = iy2 - iy1

    # 겹치는 부분이 없는 경우
    if width < 0 or height < 0:
        return 'd'
    # 교차 부분이 점인 경우
    elif width == 0 and height == 0:
        return 'c'
    # 교차 부분이 선분인 경우
    elif width == 0 and height > 0:
            return 'b'
    elif width > 0 and height == 0:
            return 'b'
    # 교차 부분이 직사각형인 경우
    elif width > 0 and height > 0:
        return 'a'

# 입력 처리
for _ in range(4):
    arr = list(map(int, input().split()))
    x1, y1, p1, q1 = arr[:4]
    x2, y2, p2, q2 = arr[4:]

    print(intersection_type(x1, y1, p1, q1, x2, y2, p2, q2))