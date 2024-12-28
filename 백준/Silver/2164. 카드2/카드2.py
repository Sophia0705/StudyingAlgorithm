from collections import deque

n = int(input())
cards = deque(i for i in range(1, n+1))
while cards:
    if len(cards) == 1:
        print(*cards)
    cards.popleft()
    if cards:
        t = cards.popleft()
        cards.append(t)
