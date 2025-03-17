import sys
input = sys.stdin.readline

n = int(input())
books = {}

for _ in range(n):
    title = input()
    if title in books:
        books[title] += 1
    else:
        books[title] = 1

# 가장 많이 팔린 책 찾기
max_sold = 0
best_seller = ""

for title, count in books.items():
    # 현재 책이 더 많이 팔렸거나
    # 같은 횟수로 팔렸지만 사전 순으로 더 앞서는 경우
    if count > max_sold or (count == max_sold and title < best_seller):
        max_sold = count
        best_seller = title

print(best_seller)