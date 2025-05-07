"""
단지번호붙이기
https://www.acmicpc.net/problem/2667
실버1
"""
import sys
from collections import deque

#방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS 메서드 정의
def bfs(graph, start, N):
    queue = deque([start])
    graph[start[0]][start[1]] = 0 # 방문처리
    count = 1

    #큐가 빌 때까지 반복
    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어날 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
                
            # 이동할 수 없는 칸 무시
            if graph[nx][ny] == 0:
                continue

            # 이동 가능 시 방문 처리 
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            start = (i,j)
            result.append(bfs(graph, start, N))

result.sort()

print(len(result)) # 총 단지 수
for r in result:
    print(r) # 각 단지의 집 수