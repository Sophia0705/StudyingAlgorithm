# 5597. 과제 안 내신 분..?

submitted = [int(input()) for _ in range(28)]
students = [i for i in range(1, 31)]

submitted_set = set(submitted)
students_set = set(students)

ans_set = students_set - submitted_set
ans = list(ans_set)
ans.sort()

for i in ans:
    print(i)
