def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] not in s[0:i]:
            answer.append(-1)
        else:
            answer.append(i-s[0:i].rindex(s[i]))
    return answer