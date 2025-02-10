from itertools import permutations

def solution(numbers):
    answer = 0
    used = set()    # 중복 체크용
    
    # 소수 판별
    def check(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    # 숫자 만들기
    for i in range(1, len(numbers)+1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))    # str -> int
            if num not in used:
                used.add(num)
                if check(num):
                    answer += 1
    return answer