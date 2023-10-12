# # SWEA Solving Club 알뜰 기차 여행

# # 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자
# import heapq

# # 입력
# N, T = map(int, input().split())
# # 인접 리스트
# graph = [[] for i in range(N)]
# for _ in range(T):
#     a, b, w = map(int, input().split())
#     graph[a].append([b, w])

# # 1. 누적거리를 계속 저장
# INF = int(1e9)  # 최대값으로 1억 - 대충 엄청 큰 수
# distance = [INF] * N


# def dijkstra(start):
#     # 2. 우선순위 큐
#     pq = []
#     # 출발점 초기화
#     heapq.heappush(pq, (0, start))
#     distance[start] = 0

#     while pq:
#         # 현재 시점에서 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
#         dist, now = heapq.heappop(pq)

#         # 이미 방문한 지점 + 누적거리가 더 짧게 방문한 적이 있다면 pass
#         if distance[now] < dist:
#             continue

#         # 인접 노드를 확인
#         for next in graph[now]:
#             next_node = next[0]
#             cost = next[1]

#             # next_node 로 가기 위한 누적거리
#             new_cost = dist + cost

#             # 누적 거리가 기존보다 크네?
#             if distance[next_node] <= new_cost:
#                 continue

#             distance[next_node] = new_cost
#             heapq.heappush(pq, (new_cost, next_node))


# dijkstra(0)
# ans = distance[N - 1]
# if ans == INF:
#     ans = 'impossible'
# print(ans)



arr = [1, 2, 3, 4, 5]
n = len(arr)
cnt = 0
for i in range(1, 1 << (n-1)):
    
    area1 = []
    area2 = []
    for j in range(n):
        if i & (1 << j):
            area1.append(arr[j])
        else:
            area2.append(arr[j])
    print(area1, end=' / ')
    print(area2, end='\n')
    cnt += 1
    print(cnt)









































