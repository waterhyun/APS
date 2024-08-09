# 4880. [기본] 5일차 - 토너먼트 카드게임 (제출용) D2

def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수 구현
 
def win(p1, p2):
    p1_v = arr[p1]
    p2_v = arr[p2]
 
    # p1이 이기는 조건 리스트
    p1_l = [1, 2, 3]
    p2_l = [3, 1, 2]
 
    if p1_l.index(p1_v) == p2_l.index(p2_v):
        return p1
    # if (p1_v == 1 and p2_v ==3) or (p1_v == 2 and p2_v == 1) or (p1_v == 3 and p2_v ==2):
    #     return p1
    elif p1_v == p2_v:
        return p1
    else:
        return p2
 
tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    result = f(1, n)
    print(f'#{t} {result}')