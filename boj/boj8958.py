tc = int(input())
for _ in range(tc):
    ox = list(input())
    cnt = 0
    result = 0
    for a in ox:
        if a == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)


