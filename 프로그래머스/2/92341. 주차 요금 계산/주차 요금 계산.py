from collections import defaultdict
import math

def solution(fees, records):
    # 시간 분으로
    def time2min(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours*60 + minutes
    
    parking_start = {}  # 입차시간 딕셔너리
    total_time = defaultdict(int)   # 차량별 총 주차시간 딕셔너리
    
    # 입/출차 기록 
    for record in records:
        time, car_num, status = record.split()
        minutes = time2min(time)
        
        if status == 'IN':
            parking_start[car_num] = minutes
        
        else:
            total_time[car_num] += minutes - parking_start[car_num]
            del parking_start[car_num]
    
    # 출차 기록 없는 차
    for car_num, in_time in parking_start.items():
        total_time[car_num] += time2min('23:59') - in_time
        
    # 요금 계산
    def cal_fee(total_minutes):
        if total_minutes <= fees[0]:
            return fees[1]  # 기본 요금
        else:
            extra_time = math.ceil((total_minutes - fees[0]) / fees[2])
            return fees[1] + extra_time * fees[3]
    
    # 차량번호 순으로 정렬해서 요금 계산
    answer = []
    for car_num in sorted(total_time.keys()):
        answer.append(cal_fee(total_time[car_num]))
    return answer