# 3499. 퍼펙트 셔플

tc = int(input())  # 테스트 케이스

for t in range(1, tc+1):
    n = int(input())  # 1 ≤ N ≤ 1,000, N개의 카드
    cards = list(input().split())

    # 카드가 짝수일 때
    if n % 2 == 0:
        mid = n//2
    else:
        mid = n // 2 + 1

    left = cards[0:mid]
    right = cards[mid:]

    sorted_cards = [0] * n
    flag = 0
    for i in range(n):
        if i % 2 == 0:
            sorted_cards[i] = left[i//2]
            flag += 1
        else:
            sorted_cards[i] = right[i//2]
            flag += 1

    print(f'#{t}', *sorted_cards)