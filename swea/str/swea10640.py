# 4864. 3일차 - 문자열 비교 (제출용) D1

def BruteForce(str1, str2):
    i = 0 # A의 인덱스
    j = 0 # B의 인덱스
    n = len(str2) # 전체 텍스트의 길이
    m = len(str1) # 패턴의 길이
 
    while i < n:
        if str2[i] == str1[j]:
            i += 1
            j += 1
            if j == m:
                return 1 # 패턴 찾음
        else:
            i = i - j + 1 # 다음 위치로!
            j = 0
    return 0 # 패턴 못찾음
 
tc = int(input())
for t in range(1, tc+1):
    str1 = input()
    str2 = input()
    result = BruteForce(str1, str2)
    print(f'#{t} {result}')