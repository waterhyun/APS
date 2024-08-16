# 5789. 현주의 상자 바꾸기

tc = int(input())
for t in range(1, tc+1):
    n, q = map(int, input().split())
    box = [0 for _ in range(0, n+1)]
    
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            box[j] = i
    
    result = box[1:]

    print(f'#{t}', *result)