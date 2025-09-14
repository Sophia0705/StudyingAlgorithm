def solution(want, number, discount):
    answer = 0
    todo = dict()   # 장볼 것
    for i in range(len(want)):
        todo[want[i]] = number[i]
    
    for i in range(len(discount)-9):  # 10일 끊어서 보기
        check = dict()
        for j in range(i, i+10):
            if discount[j] in todo:
                check[discount[j]] = check.get(discount[j], 0) +1
        if check == todo:
            answer += 1
        
    return answer