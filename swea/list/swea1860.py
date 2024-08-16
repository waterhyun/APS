# 1860. 진기의 최고급 붕어빵

#  N명의 사람이 자격
# 0초부터 붕어빵을 만들기 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
# 0초 이후에 손님들이 언제 도착하는지 주어지면, 
# 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램을 작성하라.
def f(N, M, K):
    for i in range(N):
        if t[i]//M*K < i+1:  #  t[i]//M(i 손님 도착시간까지 생산횟수) * K (회당 생산 수) < i+1 (i는 0부터, i+1 손님수)
            return 'Impossible'
    return 'Possible'
 
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N 명의 손님, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있음.
    t = list(map(int, input().split()))
    t.sort()    # 도착 시간별로 방문 인원수를 파악하기 위해 오름차순 정렬
    print(f'#{tc} {f(N, M, K)}')

#########################################################################

tc = int(input())
for t in range(1, tc + 1):
    N, M, K = map(int, input().split())  # N, M, K(1 ≤ N, M, K ≤ 100)가 공백으로 구분
    arr = sorted(list(map(int, input().split())))
    count = [0] * 11112

    flag = True
    if arr.count(0) > 0:
        flag = False
    else:
        for i in range(1, max(arr)+1):
            if i % M == 0:
                count[i] += count[i - 1] + K
            else:
                count[i] += count[i - 1]
            if len(arr) != 0 and arr[0] == i:
                a = arr.pop(0)
                if a == 0:
                    flag = False
                    break
                if count[i] < 1:
                    flag = False
                    break
                else:
                    count[i] -= 1
            if len(arr) == 0:
                break

    if flag:
        print(f"#{t} Possible")
    else:
        print(f"#{t} Impossible")

