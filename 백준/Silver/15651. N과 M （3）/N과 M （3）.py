from itertools import product

n, m = map(int, input().split())

numbers = [i for i in range(1, n+1)]

for num in product(numbers, repeat=m):    # 중복 허용
    print(*num)