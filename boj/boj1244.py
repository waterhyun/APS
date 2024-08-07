# 스위치 켜고 끄기, 실버 4

pcs = int(input()) # 스위치 개수
state = list(map(int, input().split())) # 스위치 상태
people = int(input()) # 사람 수

# 남학생의 스위치 동작
def man():
    global num, pcs, state
    for i in range(num-1, pcs, num):
        state[i] = 1 - state[i]

# 여학생의 스위치 동작
def woman():
    global num, state, pcs
    start = num - 2
    end = num

    # 범위가 유효한지 확인
    while start >= 0 and end < pcs and state[start] == state[end]:
        start -= 1
        end += 1

    # 마지막으로 유효한 범위로 조정
    start += 1
    end -= 1

    for i in range(start, end + 1):
        print(i)
        state[i] = 1 - state[i]  # 상태 반전


for _ in range(people):
    sex, num = map(int, input().split())
    if sex == 1:
        man()
        print(*state)
    else:
        woman()
        print(*state)

for i in range(0, len(state), 20):
    print(*state[i:i+20])

# 0 0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 1 1 1 0 0 1 0 1