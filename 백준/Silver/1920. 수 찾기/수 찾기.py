n = int(input())
A = list(map(int, input().split()))
nA = set(A)
m = int(input())
arr = list(map(int, input().split()))

for num in arr:
    if num in nA:
        print(1)
    else:
        print(0)
