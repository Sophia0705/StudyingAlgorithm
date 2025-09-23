import math
def solution(n, m):
    gcd = math.gcd(n, m)
    # 두 수의 곱은 '최대공약수와 최소공배수의 곱'과 같다
    lcm = n * m / gcd
    return [gcd, lcm]