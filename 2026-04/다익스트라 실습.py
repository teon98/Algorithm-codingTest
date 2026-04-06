"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3 
4 5 1
5 3 1
5 6 2
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

print(graph)
print(distance)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 경우 건너뛰기
        if distance[now] < dist: 
            continue 
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, n+1):
    #도달할 수 없는 경우, 무한(INFINITY)라고 출력.
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])