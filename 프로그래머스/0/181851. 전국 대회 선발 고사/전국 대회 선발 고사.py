def solution(rank, attendance):
    stu = {}
    
    for idx in range(len(rank)):
        if attendance[idx]:
            stu[idx] = rank[idx]    # 번호 : 등수
    
    # 등수별로 정렬해서
    sorted_stu = sorted(stu.items(), key=lambda x: x[1])
    
    # 앞에 세 개만 하면 그게 a, b, c -> answer
    a = sorted_stu[0][0]
    b = sorted_stu[1][0]
    c = sorted_stu[2][0]
    
    answer = 10000 * a + 100 * b + c
    return answer