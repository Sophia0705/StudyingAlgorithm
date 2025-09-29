def solution(name, yearning, photo):
    answer = []
    missing_points = dict()
    for i in range(len(name)):
        missing_points[name[i]] = yearning[i]
    
    
    for pic in photo:
        score = 0
        for person in pic:
            if person in missing_points.keys():
                score += missing_points[person]
        answer.append(score)
    return answer