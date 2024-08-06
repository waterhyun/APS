# 파스칼의 삼각형 D2
def pascal(n):
    if n == 1:
        return [1]
    else:
        remain = pascal(n-1)
        return [1] + [remain[i] + remain[i+1] for i in range(len(remain)-1)] + [1]

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    print(f'#{t}')
    for i in range(1, n+1):
        print(*pascal(i))

    