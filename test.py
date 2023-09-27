# i : 현재 행, N : 전체 행의 수, s: 현재까지의 점수 합
def func(i, N, s):
    global max_v
    if i == N:  # 모든 행을 다 본 경우
        if max_v < s:
            max_v = s

    else:
        for j in range(i, N): # 현재 행 부터 마지막 행까지 순회
            p[i], p[j] = p[j], p[i]
            # 재귀 호출로 다음 행으로 넘어가며 점수를 더해준다.
            func(i+1, N, s+arr[i][p[i]])
            # 백트래킹 (원래 순서로 바꿔줌)
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]   # 초기 순서 저장하는 리스트 P
    max_v = 0
    func(0, N, 0)
    print(f'#{tc} {max_v}')
