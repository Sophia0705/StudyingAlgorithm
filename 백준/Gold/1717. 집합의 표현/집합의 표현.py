# 1717 집합의 표현
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def check(x):
    if parent[x] != x:
        parent[x] = check(parent[x])
    return parent[x]

def union(a, b):
    a = check(a)
    b = check(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]    # 각 원소의 부모를 자기 자신으로
for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a, b) # 합집합
    elif cal == 1:
        if check(a) == check(b):
            print("YES")
        else:
            print("NO")