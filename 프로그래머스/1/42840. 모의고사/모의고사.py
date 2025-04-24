def solution(answers):
    correct = []
    c1 = c2 = c3 = 0
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            c1 += 1
        if answers[i] == p2[i % len(p2)]:
            c2 += 1
        if answers[i] == p3[i % len(p3)]:
            c3 += 1
            
    maxV = max(c1, c2, c3)
    if c1 == maxV:
        correct.append(1)
    if c2 == maxV:
        correct.append(2)
    if c3 == maxV:
        correct.append(3)
    return correct