def solution(strings, n):
    sorted_str = sorted(strings, key=lambda x: (x[n], x))
    return sorted_str