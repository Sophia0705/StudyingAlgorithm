def solution(sizes):
    maxW, maxH = 0, 0   # 긴 변들 중 최대, 짧은 변들 중 최대
    
    for size in sizes:
        w, h = max(size), min(size)
        
        if w >= maxW:
            maxW = w
        if h >= maxH:
            maxH = h
            
    return maxW * maxH