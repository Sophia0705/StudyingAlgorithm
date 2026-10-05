def solution(my_string):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    counts = {a: 0 for a in alphabet}
    
    
    for c in my_string:
        counts[c] += 1
    answer = list(counts.values())
    return answer