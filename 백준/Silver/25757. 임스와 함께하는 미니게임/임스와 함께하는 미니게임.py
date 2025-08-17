# 25757. 임스와 함께하는 미니게임
import sys
input = sys.stdin.readline

N, type = input().split()   # type) Y: 2, F: 3, O: 4
N = int(N)
players = set(input().strip() for _ in range(N))

if type == 'Y':
    print(len(players))
elif type == 'F':
    print(len(players) // 2)
elif type == "O":
    print(len(players) // 3)