def get_puzzle_time(diff, time_cur, time_prev, level):
    if diff <= level:
        return time_cur
    else:
        fail_count = diff - level
        return (time_cur + time_prev) * fail_count + time_cur

def can_solve_all(diffs, times, limit, level):
    total_time = 0
    
    for i in range(len(diffs)):
        time_cur = times[i]
        time_prev = times[i-1] if i > 0 else 0
        puzzle_time = get_puzzle_time(diffs[i], time_cur, time_prev, level)
        
        total_time += puzzle_time
        if total_time > limit:
            return False
            
    return True

def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if can_solve_all(diffs, times, limit, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer