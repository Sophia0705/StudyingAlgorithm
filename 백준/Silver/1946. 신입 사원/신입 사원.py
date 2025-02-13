import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(N)]

    # score1 기준으로 정렬
    applicants.sort()

    count = 1  # 첫 번째 사람은 무조건 선발
    min_score2 = applicants[0][1]  # 첫 사람의 면접 점수

    # 두 번째 사람부터 확인
    for score1, score2 in applicants[1:]:
        if score2 < min_score2:  # 이전까지의 최소 면접 점수보다 더 좋은 점수라면
            count += 1  # 선발 인원 증가
            min_score2 = score2  # 최소 면접 점수 갱신

    print(count)