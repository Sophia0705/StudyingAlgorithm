from itertools import permutations

def check(nums):
    for i in range(k):
        if signs[i] == '<':
            if nums[i] > nums[i+1]:
                return False
        else:
            if nums[i] < nums[i+1]:
                return False
    return True

k = int(input())    # k: 부등호 문자 개수
signs = input().split()
nums = list(range(0, 10))
all = list(permutations(nums, k+1))
ans = []

for case in all:
    if check(case):
        ans.append(''.join(map(str, case)))

print(max(ans))
print(min(ans))

