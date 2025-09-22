def solution(sizes):
    w, h = [], []
    
    for size in sizes:
        max_side = max(size)
        min_side = min(size)
        
        w.append(max_side)
        h.append(min_side)
    
    return max(w)*max(h)