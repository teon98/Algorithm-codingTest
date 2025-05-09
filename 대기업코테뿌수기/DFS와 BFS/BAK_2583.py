"""
문제: 영역 구하기
링크: https://www.acmicpc.net/problem/2583
난이도: 실버1
푼 날짜: 2025.05.07
"""
import sys
from collections import deque

def bfs(graph, start, M, N):
    queue = deque([start])
    graph[start[0]][start[1]] = 0 #첫 방문 처리

    #방향 정의(상,하,좌,우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #넓이 구하기
    count = 1

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #영역 범위 밖
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
                
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    
    return count

input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[1] * N for _ in range(M)] 

#직사각형이 그려지는 영역 -> 통과할 수 없는 영역(0)
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 0

result = []
# 1로 시작하는 부분 찾기
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            start = (i, j)
            result.append(bfs(graph, start, M, N)) #graph 참조 전달

result.sort()

print(len(result))
print(*result) #unpacking



