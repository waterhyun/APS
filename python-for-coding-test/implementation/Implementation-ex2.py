# 시각

# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하기.

h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for l in range(60):
            if '3' in str(i) + str(j) + str(l):
                count += 1

print(count)
