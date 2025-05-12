"""
문제: 토마토2
링크: https://www.acmicpc.net/problem/7569
난이도: 골드5
푼 날짜: 2025.05.12

1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 X
"""
import sys
from collections import deque

def bfs(graph, visited, start, M, N, H):
    queue = deque([])

    for start_node in start:
        queue.append(start_node)

    last_day = 0

    while queue:
        h, y, x, d = queue.popleft() 

        #방향 정의
        direction = [(0,0,-1), (0,0,1), (0,-1,0), (0,1,0), (-1,0,0), (1,0,0)]

        for dh, dy, dx in direction:
            nh = h + dh
            ny = y + dy
            nx = x + dx

            if nh < 0 or ny < 0 or nx < 0 or nh >= H or ny >= N or nx >=M:
                continue

            if graph[nh][ny][nx] == 0 and visited[nh][ny][nx] == False:
                visited[nh][ny][nx] = True
                queue.append((nh, ny, nx, d+1))
                last_day = d+1

    return last_day

input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = []
for _ in range(H):
    box = []
    for _ in range(N):
        box_input = list(map(int, input().split()))
        box.append(box_input)
    graph.append(box)

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

# 익은 토마토 찾기
start = []
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                visited[h][n][m] = True
                start.append((h, n, m, 0))
            elif graph[h][n][m] == -1:
                visited[h][n][m] = True

# BFS 타기
result = bfs(graph, visited, start, M, N, H)
is_all_True = True

# 모든 토마토가 익지 않은 경우 찾기
for box in visited:
    for row in box:
        if False in row:
            is_all_True = False
            break

if is_all_True:
    print(result)
else:
    print(-1)