# 삼성시의 버스 노선 D3

tc = int(input()) # 테스트 케이스
for t in range(1, tc+1):
    n = int(input()) # 버스 개수
    
    counts = [0] * 5001
    # n개의 노선 정보를 모두 읽어놓고 처리 or 읽을 때 마다 처리
    for _ in range(n): # 읽을 때마다 처리
        A, B = map(int, input().split()) # Ai -> Bi 버스 노선의 시작점 Ai와 종점 Bi, Ai <= Bi
        for i in range(A, B+1): # 1 <= Ai <= Bi <= 5,000
            counts[i] += 1


    P = int(input())  # 노선수를 출력할 P개의 버스 정류장
    # 모두 읽어놓고 처리
    bus_stop = [int(input()) for _ in range(P)]
    print(f'#{t}', end = " ")
    for j in bus_stop: # 노선수를 출력할 정류장 번호
        print(counts[j], end= ' ')
    print()