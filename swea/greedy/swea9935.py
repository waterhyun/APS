import sys
sys.stdin = open('swea\input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    # 24시간 운영되는 물류센터
    # 화물을 싣고 내리는 도크
    # 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록
    # 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램

    N = int(input())  # 신청서
    times = list(tuple(map(int, input().split())) for _ in range(N))
    times.sort(key = lambda x : x[1])
    # print(times)
    
    cnt = 0
    last_time = 0
    for t in times:
        s, e = t
        if s >= last_time:
            cnt += 1
            last_time = e
    
    print(f'#{tc} {cnt}')

            
