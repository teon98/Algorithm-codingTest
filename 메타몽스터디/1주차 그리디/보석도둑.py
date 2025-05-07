import sys
import heapq

input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().split())  # 보석 개수, 가방 개수
jewels = []
bags = []

# 보석 정보 입력
for _ in range(N):
    m, v = map(int, input().split())  # 무게, 가격
    jewels.append((m, v))

# 가방 정보 입력
for _ in range(K):
    bags.append(int(input().strip()))

# 보석과 가방 정렬
jewels.sort()  # 무게를 기준으로 오름차순 정렬
bags.sort()    # 용량을 기준으로 오름차순 정렬

# 최대 힙을 위한 리스트
max_heap = []
total_value = 0
jewel_index = 0

# 각 가방에 대해 처리
for bag in bags:
    # 현재 가방에 넣을 수 있는 보석들을 최대 힙에 추가
    while jewel_index < N and jewels[jewel_index][0] <= bag:
        heapq.heappush(max_heap, -jewels[jewel_index][1])  # 가격을 음수로 넣어서 최대 힙처럼 사용
        jewel_index += 1

    # 힙에서 가장 비싼 보석을 선택
    if max_heap:
        total_value += -heapq.heappop(max_heap)

# 출력
print(total_value)
