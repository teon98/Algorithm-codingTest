"""
LINK: https://www.acmicpc.net/problem/2178
DATE: 2025.08.07
"""
import sys
from collections import deque

#방향 정의(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph, N, M, start):
    queue = deque([start])

    #큐가 빌 때까지 반복
    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어날 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            # 이동할 수 없는 칸 무시
            if graph[nx][ny] == 0:
                continue

            # 이동 가능 시 방문 처리 
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                print(graph)
                queue.append((nx, ny))
    
    return graph[N-1][M-1]

input = sys.stdin.readline
N, M = map(int, input().split())

graph = []

for _ in range(N):
    line = list(map(int, input().strip()))
    graph.append(line)

start = (0,0)
result = bfs(graph, N, M, start)
print(result)