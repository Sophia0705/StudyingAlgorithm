def solution(k, score):
    answer = []
    fame = []
    
    for s in score:
        fame.append(s)
        fame.sort(reverse=True)
        last = fame[:k][-1]
        answer.append(last)
        
    return answer