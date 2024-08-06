# 가장 빠른 문자열 타이핑 

def BruteForce(A, B):
    i = 0 # A의 인덱스
    j = 0 # B의 인덱스
    n = len(A) # 전체 텍스트의 길이
    m = len(B) # 패턴의 길이
    idx_list = []
 
    while i < n:
        if A[i] == B[j]:
            i += 1
            j += 1
            if j == m:
                idx_list.append(i - m)  # 패턴이 발견된 위치
                j = 0  # 패턴 인덱스 초기화
        else:
            i = i - j + 1 # 다음 위치로!
            j = 0
 
    return idx_list
 
tc = int(input())
for t in range(1, tc+1):
    A, B = input().split()
    idx_list = BruteForce(A, B)
 
    cnt = 0
    last_idx = 0
    if not idx_list: # 패턴이 없을 경우
        cnt = len(A)
 
    for idx in idx_list: # 패턴이 발견된 위치에 따라
        cnt += (idx - last_idx) # 패턴 발견 전은 하나씩 카운트
        cnt += 1 # 패턴 타이핑 횟수
        last_idx = idx + len(B) # 다음 타이핑 시작 위치
 
    cnt += (len(A) - last_idx) # 남은 문자열 처리
    print(f'#{t} {cnt}')