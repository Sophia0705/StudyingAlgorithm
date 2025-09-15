def solution(x, n): # x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트
    answer = []
    cur = x
    for _ in range(n):
        answer.append(cur)
        cur += x
    
    return answer