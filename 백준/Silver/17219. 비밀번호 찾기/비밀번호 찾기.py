import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pwdict = {}
for _ in range(n):
    line = input().strip()
    email, pw = line.split()
    pwdict[email] = pw  # email: key, pw: value

for _ in range(m):
    email = input().strip()
    print(pwdict[email])