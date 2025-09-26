import math
def isprime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    nums = [i for i in range(1, n+1)]
    for num in nums:
        if isprime(num):
            answer += 1
    return answer