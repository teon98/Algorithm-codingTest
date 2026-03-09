import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())  # 센서의 개수
K = int(input())  # 기지국의 개수

# 센서 위치 입력
sensors = list(map(int, input().split()))

# 예외 처리: 센서 개수보다 기지국이 많거나 같으면 거리는 0
if K >= N:
    print(0)
    sys.exit()

# 센서 위치 정렬
sensors.sort()

# 거리 차이를 계산
distances = []
for i in range(1, N):
    distances.append(sensors[i] - sensors[i - 1])

# 거리 차이를 내림차순 정렬
distances.sort(reverse=True)

# 가장 긴 거리 K-1개를 제거하고 나머지 거리 합을 계산
result = sum(distances[K-1:])

# 결과 출력
print(result)