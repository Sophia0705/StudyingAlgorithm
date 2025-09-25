from itertools import combinations
import math
def check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    comb = combinations(nums, 3)
    
    for c in comb:
        if check(sum(c)):
            answer += 1

    return answer