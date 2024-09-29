from itertools import permutations

n, m = map(int, input().split())

numbers = [i for i in range(1, n+1)]

for perm in permutations(numbers, m):
    print(*perm)