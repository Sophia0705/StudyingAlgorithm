n = int(input())
tuples = []
ranks = []
for _ in range(n):
    x, y = map(int, input().split())
    tuples.append((x, y))

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j:  # 자기 빼고 비교
            # 덩치 비교
            if tuples[i][0] < tuples[j][0] and tuples[i][1] < tuples[j][1]:
                rank += 1
    ranks.append(rank)

print(*ranks)