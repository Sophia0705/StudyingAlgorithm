num_list = [int(input()) for _ in range(9)]
maxN = max(num_list)
idx = 0
for n in num_list:
    if n == maxN:
        idx += 1
        break
    else:
        idx += 1
print(maxN)
print(idx)