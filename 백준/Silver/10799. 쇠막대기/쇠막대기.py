# 10799. 쇠막대기
import sys
input = sys.stdin.readline

strs = input().rstrip()
st = []
cnt = 0

for i in range(len(strs)):
    if strs[i] == '(':
        st.append('(')
    else:
        if strs[i-1] == '(':
            st.pop()
            cnt += len(st)

        else:
            st.pop()
            cnt += 1

print(cnt)