# 팔

L, R = input().split()

# L과 R의 자릿수가 다르면 무조건 최소값 0
if len(L) != len(R):
    print(0)
else:
    min_v = 0
    
    # 앞에서부터 비교하여 처음 다른 숫자가 나오기 전까지 '8' 개수 찾기
    for i in range(len(L)):
        if L[i] != R[i]:  # 다른 숫자가 나오면 뒤는 무조건 포함될 수 있음
            break
        if L[i] == '8':  # 공통된 부분에서만 '8' 카운트
            min_v += 1

    print(min_v)
