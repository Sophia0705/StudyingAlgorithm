def solution(a, b, n):
    answer = 0
    
    while n >= a:
        excnt = n // a
        getcola = excnt * b
        answer += getcola
        
        n = getcola + (n % a)
    return answer