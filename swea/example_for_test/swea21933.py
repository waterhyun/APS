# 21933. 배열 합치기

# 100 이하의 자연수가 들어있는 두 배열 A, B의 원소를 배열 C에 모두 옮기려고 한다
# 옮길 때는 A와 B의 원소를 빠른 인덱스 순으로 교대로 C에 옮겨야 하며, 
# 크기가 작은 배열의 원소가 모두 옮겨지면 남은 배열의 원소는 연속으로 C로 옮기면 된다. 
# A, B의 원소가 주어지면, 규칙에 따라 C로 옮긴 후 C의 원소를 모두 출력하는 프로그램을 작성하라.
# 배열 C의 크기는 A와 B의 크기를 더한 것과 항상 같다.

tc = int(input())
for t in range(1, tc+1):
    N, M = map(int, input().split())  # A와 B의 원소 개수 N과 M, (1 <= N, M <=100)
    A = list(map(int, input().split()))  
    B = list(map(int, input().split()))

    C = []
    for i in range(N+M):
        if len(A) > 0 :
            a = A.pop(0)
            C.append(a)
        if len(B) > 0 :
            b = B.pop(0)
            C.append(b)
    
    print(f'#{t}', *C)
