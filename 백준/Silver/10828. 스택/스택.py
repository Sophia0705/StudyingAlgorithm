import sys

n = int(input())
stack = []
for _ in range(n):
    do = sys.stdin.readline().rstrip()
    if 'push' in do:
        push, X = do.split()
        X = int(X)
        stack.append(X)
    elif do == 'pop':
        if stack:
            a = stack[-1]
            stack.pop(-1)
            print(a)
        else:
            print(-1)
    elif do == 'size':
        print(len(stack))
    elif do == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif do == 'top':
        if stack:
            b = stack[-1]
            print(b)
        else:
            print(-1)
