import sys
input = sys.stdin.readline

m = int(input())
S = 0
for _ in range(m):
    command = input().rstrip().split()
    op = command[0]

    if op == 'all':
        S = (1 << 20) -1    # 20개의 비트를 모두 1로 설정
    elif op == 'empty':
        S = 0
    else:   # x 있을 때
        x = int(command[1]) -1

        if op == 'add':
            S |= (1 << x)
        elif op == 'remove':
            S &= ~(1 << x)
        elif op == 'check':
            print(1 if S & (1 << x) else 0)
        elif op == 'toggle':
            S ^= (1 << x)