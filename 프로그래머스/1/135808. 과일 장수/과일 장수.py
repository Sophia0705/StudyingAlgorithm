def solution(k, m, score):
    answer = 0
    # 한 상자에 m개씩 포장 -> 각 상자의 가장 낮은 점수 p * m = 이익
    # score를 sort하고
    score.sort(reverse=True)
    # score 배열을 m개씩 나누기 & m개씩 중에서 낮은 점수를 최대화
    for i in range(0, len(score), m):   # m개씩 끊어서
        if i + m <= len(score):
            profit = score[i + m -1] * m
            answer += profit
    return answer