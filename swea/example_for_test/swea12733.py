# 12733. 기지국
tc = int(input())  # 테스트케이스
for t in range(1, tc+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    # 집이 위치한 원소는 H
    # 기지국이 위치한 원소는 'A', 'B', 'C'로 표시하며
    # 각각 동서남북으로 1, 2, 3개를 커버하는 기지국이다.
    # 'X' 원소는 아무것도 없다는 것을 의미한다.

    abc = {'A': 1, 'B': 2, 'C': 3, 'H': 4, 'X': 0}
    di = [0, +1, 0, -1]
    dj = [1, 0, -1, 0]
    house_set = set()
    visited_set = set()
    for i in range(n):
        for j in range(n):
            if abc[arr[i][j]] == 4:
                house_set.add((i, j))
            if abc[arr[i][j]] in [1, 2, 3]:
                for k in range(4):
                    for l in range(1, abc[arr[i][j]]+1):
                        ni = i + di[k]*l
                        nj = j + dj[k]*l
                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'H':
                            visited_set.add((ni, nj))

    result = len(house_set)-len(visited_set)
    print(f'#{t} {result}')