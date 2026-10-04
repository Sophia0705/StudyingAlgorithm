import sys
sys.set_int_max_str_digits(100000) # 제한을 10만 자리 이상으로 확장

def solution(a, b):
    answer = int(a) + int(b)
    return str(answer)