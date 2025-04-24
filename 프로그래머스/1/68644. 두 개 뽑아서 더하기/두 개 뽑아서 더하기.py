def solution(numbers):
    answer = []
    sumV = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sumV = numbers[i] + numbers[j]
            if sumV not in answer:
                answer.append(sumV)
    answer.sort()
    return answer