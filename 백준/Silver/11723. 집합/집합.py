import sys
input = sys.stdin.readline

def solve(do, x=None):
    global S
    if do == 'add' and x not in S:
        S.add(x)
    elif do == 'remove' and x in S:
        S.remove(x)
    elif do == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif do == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif do == 'all':
        S = set(str(i) for i in range(1, 21))
    elif do == 'empty':
        S.clear()

m = int(input())
S = set()
for _ in range(m):
    command = input().rstrip().split()
    do = command.pop(0)
    if command:
        x = command[0]
        solve(do, x)
    else:
        solve(do)