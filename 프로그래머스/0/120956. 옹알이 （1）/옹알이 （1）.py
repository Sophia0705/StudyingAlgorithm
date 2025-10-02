def solution(babbling):
    answer = 0
    pronounces = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        temp = word
        # 가능한 발음 순회하며 공백으로 치환
        for p in pronounces:
            temp = temp.replace(p, ' ')

        # 치환된 문자열에서 공백 제거 -> 빈 문자열이면 발음 가능(answer += 1)
        if temp.replace(' ', '') == '':
            answer += 1
    
    return answer