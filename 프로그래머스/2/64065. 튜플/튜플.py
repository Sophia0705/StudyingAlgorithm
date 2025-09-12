def solution(s):
    answer = []
    seen = set()
    tuples = s[2:-2].split('},{')
    tuples.sort(key=len)    # 튜플 길이 기준 정렬
    
    for t in tuples:
        numbers = map(int, t.split(','))
        for num in numbers:
            if num not in seen:
                answer.append(num)
                seen.add(num)
    return answer