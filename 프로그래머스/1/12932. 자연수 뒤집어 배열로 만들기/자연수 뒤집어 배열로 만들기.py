def solution(n):
    answer = []
    reversed_n = str(n)[::-1]
    for c in reversed_n:
        answer.append(int(c))
    return answer