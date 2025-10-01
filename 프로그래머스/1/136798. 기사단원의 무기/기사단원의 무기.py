import math

def find_divisor(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            cnt += 1
            if n // i != i:
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = 0
    knights = [i for i in range(1, number+1)]
    for knight in knights:
        supposed = find_divisor(knight)
        if supposed > limit:
            answer += power
        else:
            answer += supposed
    return answer