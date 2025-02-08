from itertools import combinations

def get_dist(houses, chicks):
    total = 0
    for hx, hy in houses:
        min_dist = float('inf')
        for cx, cy in chicks:
            min_dist = min(min_dist, abs(hx - cx) + abs(hy - cy))
        total += min_dist
    return total

def solve(n, m, city):
    houses, chicks = [], []

    for r in range(n):
        for c in range(n):
            if city[r][c] == 1:
                houses.append((r, c))
            elif city[r][c] == 2:
                chicks.append((r, c))

    return min(get_dist(houses, c_set) for c_set in combinations(chicks, m))

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, m, city))
