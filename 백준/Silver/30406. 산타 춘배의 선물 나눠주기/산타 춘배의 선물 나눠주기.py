from collections import Counter

def solve(n, prices):
    # 가격별 개수 세기
    count = Counter(prices)
    total = 0

    # 가능한 XOR 조합과 만족도
    xor_pairs = [
        (3, 0, 3), (3, 1, 2), (3, 2, 1), (3, 3, 0),
        (2, 0, 2), (2, 1, 3), (2, 2, 0), (2, 3, 1),
        (1, 0, 1), (1, 1, 0), (1, 2, 3), (1, 3, 2),
        (0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3)
    ]

    # 높은 XOR 값 순서대로 처리
    for x, y, xor_val in sorted(xor_pairs, key=lambda x: -x[2]):
        if count[x] > 0 and count[y] > 0:
            if x == y:
                pairs = count[x] // 2
            else:
                pairs = min(count[x], count[y])
            total += pairs * xor_val
            count[x] -= pairs
            count[y] -= pairs

    return total

# 입력
n = int(input())
prices = list(map(int, input().split()))

# 출력
print(solve(n, prices))
