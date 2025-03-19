import sys
input = sys.stdin.readline

H, M = map(int, input().split())

M -= 45 # 45분 빼기

# 분이 음수가 되면 시간 조정
if M < 0:
    M += 60  # 60분 더해주고
    H -= 1  # 1시간 빼기

# 시간이 음수가 되면 23시로 조정
if H < 0:
    H = 23

print(H, M)
