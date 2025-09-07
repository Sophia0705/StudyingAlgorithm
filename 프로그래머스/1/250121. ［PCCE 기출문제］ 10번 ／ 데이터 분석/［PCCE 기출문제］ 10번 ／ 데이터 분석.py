def solution(data, ext, val_ext, sort_by):
    answer = []
    types = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    data = sorted(data, key=lambda x: x[types[sort_by]])
    
    for val in data:
        if val[types[ext]] < val_ext:
            answer.append(val)
    return answer