import sys
input = sys.stdin.readline

l = int(input())
strs = input().strip()
M = 1234567891
r = 31
h_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
           'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
           'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
           'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
           'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 }
ans = 0

for i in range(l):
    ans += h_dict[strs[i]] * pow(r, i) % M
    ans %= M    # 여러 수 더하다보면 다시 M보다 커질 수도 있으니까

print(ans)