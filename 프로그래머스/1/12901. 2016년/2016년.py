def solution(a, b):
    # 16.1.1 = FRI
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    today = sum(days[:a-1]) + b
    dd = today % 7
    answer = weekdays[dd-1]
    return answer