import sys

n = int(input())
Q = []
for _ in range(n):
    do = sys.stdin.readline().rstrip()
    if 'push' in do:
        push, X = do.split()
        X = int(X)
        Q.append(X)
    elif do == 'pop':
        if not Q:
            print(-1)
        else:
            a = Q.pop(0)
            print(a)
    elif do == 'size':
        print(len(Q))
    elif do == 'empty':
        if not Q:
            print(1)
        else:
            print(0)
    elif do == 'front':
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif do == 'back':
        if not Q:
            print(-1)
        else:
            print(Q[-1])
