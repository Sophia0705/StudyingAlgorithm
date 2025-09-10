def solution(n):
    splits = list(str(n))
    splits.sort(reverse=True)
    answer = ''
    for num in splits:
        answer += num
    return int(answer)