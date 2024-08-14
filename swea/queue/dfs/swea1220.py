# for t in range(1, 11):

# 푸른색 1 -> N극 (위로)
# 붉은색 2 -> S극 (아래로)
# 하나만 있는 경우엔 떨어짐 => 2개 이상인 경우만 생각
    # 그런데 똑같은 색상인 경우 다 빠짐
    # 색상이 두 개가 있는지 확인 하는 것이 더 나을 듯
# 한 줄에 두 개 이상의 교착 상태가 발 생할 수도 있음
# 쌍이 생기면 교착 상태는 쌍의 수가 됨

# 줄 마다 실행!

# 한 줄 씩 해야되겠다

for t in range(1, 11):
    num = int(input()) # 항상 고정값
    table = [list(map(int, input().split())) for i in range(100)]  # 테이블
    cnt = 0
    for col in range(100):
        flag = 0
        for row in range(100):
            if table[row][col] == 1: # 1 : N극 성질을 가지는 자성체
                flag = 1  
            elif table[row][col] == 2: # 2 : S극 성질을 가지는 자성체
                if flag == 1:
                    cnt += 1
                    flag = 0
 
    print(f'#{t} {cnt}')