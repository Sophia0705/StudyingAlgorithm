def solution(points, routes):
    time_check = {}  
    point_dict = {}  
    for i, p in enumerate(points):
        point_dict[i+1] = tuple(p)
    
    def get_path(s, e):
        sx, sy = s
        ex, ey = e
        path = []
        cur_x, cur_y = sx, sy
        
        path.append((cur_x, cur_y))
        
        while cur_x != ex:
            cur_x += 1 if ex > cur_x else -1
            path.append((cur_x, cur_y))
        
        while cur_y != ey:
            cur_y += 1 if ey > cur_y else -1
            path.append((cur_x, cur_y))
        return path
    
    # 각 로봇의 전체 경로
    for r_idx, route in enumerate(routes):
        current_time = 0
        start = point_dict[route[0]]
        if 0 not in time_check:
            time_check[0] = []
        time_check[0].append(start)
        
        for i in range(len(route)-1):
            s = point_dict[route[i]]
            e = point_dict[route[i+1]]
            path = get_path(s, e)
            
            # 각 위치마다 시간 순차적으로 기록
            for j in range(1, len(path)):
                current_time += 1
                if current_time not in time_check:
                    time_check[current_time] = []
                time_check[current_time].append(path[j])
    
    answer = 0
    for time in time_check:
        positions = time_check[time]
        pos_count = {}
        for pos in positions:
            pos_count[pos] = pos_count.get(pos, 0) + 1
        
        answer += sum(1 for count in pos_count.values() if count >= 2)
    return answer