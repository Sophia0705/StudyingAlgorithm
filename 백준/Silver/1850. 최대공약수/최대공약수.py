# 최대공약수를 계산하기 위한 gcd 함수를 math 모듈에서 import합니다.
from math import gcd

# 두 수 a와 b를 입력받습니다.
# 이 두 수는 각각 문제에서 언급된 1로 이루어진 두 수 A와 B의 길이를 나타냅니다.
a, b = map(int, input().split())

# a와 b의 최대공약수를 계산합니다.
# 이 값은 결과로 출력할 1의 개수가 됩니다.
gcd_value = gcd(a, b)

# 계산된 최대공약수만큼 1을 반복하여 출력합니다.
# 이는 문제에서 요구하는 "1로만 이루어진 최대공약수"를 나타냅니다.
print('1' * gcd_value)

# 참고: 원래 코드에서는 단순히 gcd 값을 출력했지만,
# 이 문제에서는 그 값만큼의 1을 연속해서 출력해야 합니다.
# 예를 들어, gcd 값이 3이라면 '111'을 출력해야 합니다.