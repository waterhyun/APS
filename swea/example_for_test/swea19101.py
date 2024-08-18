tc = int(input())
for t in range(1, tc+1):
    sq1 = list(map(int, input().split()))  # x, y, p, q
    sq2 = list(map(int, input().split()))  # x, y, p, q

    x = max(sq1[0], sq2[0])  # x1, x2
    p = min(sq1[2], sq2[2])  # p1, p2
    y = max(sq1[1], sq2[1])  # y1, y2
    q = min(sq1[3], sq2[3])  # q1, q2

    width = p - x
    height = q - y

    if width < 0 or height < 0 :
        print(f'#{t} 4')
    elif width == height == 0:
        print(f'#{t} 3')
    elif (width > 0 and height == 0) or (width == 0 and height > 0):
        print(f'#{t} 2')
    elif width > 0 and height > 0:
        print(f'#{t} 1')
        


