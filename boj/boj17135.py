import sys
sys.stdin = open('boj/input.txt', 'r')

# 캐슬 디펜스
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 1은 적이 있는 칸
# 0은 빈칸

# 궁수의 공격으로 제거할 수 있는 적의 최대 수

# 궁수 3명 배치
# 궁수 - 성이 있는 칸
# 하나의 칸 - 최대 1명 궁수
# 각각의 턴 마다 궁수는 적 하나를 공격 가능
# 모든 궁수는 동시에 공격
# 거리가 D이하인 적 중에서 가장 가까운 적

# 궁수 배치 -> 공격 -> 남은 적 이동 -> 성이 있는 칸으로 이동 -> 게임 제외 -> 모든 적 제외되면 게임 끝

