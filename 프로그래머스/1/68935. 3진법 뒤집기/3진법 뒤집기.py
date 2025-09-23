def n2base3(n):
    if n == 0:
        return '0'
    res = ''
    while n > 0:
        remain = n % 3
        res = str(remain) + res # 앞에 붙여야 진법 되니까
        n //= 3
    return res
    
def solution(n):
    temp = n2base3(n)
    reversed_temp = temp[::-1]  # 역순
    answer = int(reversed_temp, 3)
    return answer