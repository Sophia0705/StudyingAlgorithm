def solution(d, budget):
    answer, sumV = 0, 0
    d.sort()    # for 그리디
    
    for p in d:
        sumV += p
        if sumV <= budget:
            answer += 1
        else:
            break
    return answer