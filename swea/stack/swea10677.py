# 4869. [기본] 4일차 - 종이붙이기 (제출용) D2

# 20*20인건 20*10을 2개 쌓은 것과 같음

# def cnt(size):
#     max_10_num = size // 10
#     max_20_num = size // 20
#     cnt_20 = 0
#     for i in range(max_20_num + 1):
#         for j in range(max_10_num + 1):
#             if (i * 20) + (j * 10) == size:
#                 if cnt_20 < i:
#                     cnt_20 = i
#                     print(cnt_20, j)
#                     print('###',3 ** cnt_20, cnt_20 + 1)
#
#     result = ((3 ** cnt_20) * (cnt_20 + 1)) - (cnt_20 * 2)*2
#     return result

def cnt(length):
    n = length // 10 # 10의 배수 이므로 몫만 사용하기
    tile = [1] * 2 + [0] * (n - 1) # n까지 타일 배열을 저장하기 위해 리스트 생성
    for i in range(2, n + 1):
        tile[i] = tile[i-1] + 2 * tile[i-2]
        # 예를 들어, 4cm일때
        # 3cm에서 1cm 타일 붙이기
        # 2cm에서 2cm 타일 붙이기 * 2가지 케이스
    return tile[n]

tc = int(input())
for t in range(1, tc+1):
    num = int(input())
    total = cnt(num)
    print(f'#{t} {total}')