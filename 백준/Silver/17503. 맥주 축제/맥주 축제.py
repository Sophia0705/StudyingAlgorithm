import sys
input = sys.stdin.readline

def can_drink(beers, n, m, liver_level):
    available_beers = [beer for beer in beers if beer[1] <= liver_level]

    if len(available_beers) < n:
        return False

    available_beers.sort(reverse=True, key=lambda x: x[0])
    preference_sum = sum(beer[0] for beer in available_beers[:n])
    return preference_sum >= m


def solve(n, m, k, beers):
    # 이분 탐색
    left = 1
    right = max(beer[1] for beer in beers)  # 최대 도수 레벨
    answer = -1

    while left <= right:
        mid = (left + right) // 2  # 시도해볼 간 레벨

        if can_drink(beers, n, m, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

n, m, k = map(int, input().split())
beers = []
for _ in range(k):
    preference, level = map(int, input().split())
    beers.append((preference, level))

result = solve(n, m, k, beers)
print(result)
