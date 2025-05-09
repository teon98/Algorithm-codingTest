"""
문제: 토마토1
링크: https://www.acmicpc.net/problem/7576
난이도: 골드5
푼 날짜: 2025.05.09

1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 X

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

8

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

-1
"""
import sys
from collections import deque

def bfs(graph, visited, start_list, M, N):

    queue = deque([])

    # 첫 방문 처리
    for x,y,d in start_list:
        queue.append((x,y,d))
        visited[x][y] = True

    # 방향 정의(상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    last_day = 0

    while queue:
        x, y, day = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위를 벗어나면 무시한다
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            # 토마토가 없을 경우 -> 방문 O, 무시
            if graph[nx][ny] == -1:
                visited[nx][ny] = True
                continue

            # 안 익은 토마토를 발견하면 queue에 넣기, 방문O
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                queue.append((nx, ny, day+1))
                last_day = day + 1
                visited[nx][ny] = True
            
    return last_day
        

# 입력 빠르게 하기
input = sys.stdin.readline

M, N = map(int, input().split()) # M: 상자 가로, N: 상자 세로

# 토마토 상자(graph)
graph = []
# 토마토 상자 방문여부
visited = [[False for _ in range(M)] for _ in range(N)]

# 토마토 정보 입력받기
for _ in range(N):
    tomato_line = list(map(int, input().split()))
    graph.append(tomato_line)

day_list = []
start_tomato = [] #시작 토마토 위치 찾기
result = 0

# 익은 토마토를 찾아 떠나기 
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == False:
            start_tomato.append((i,j,0))

result = bfs(graph, visited, start_tomato, M, N)
is_all_True = True # 전체 다 방문했는지 확인하기
print(visited)

for row in visited:
    if False in row:
        is_all_True = False
        break

if is_all_True: # 모든 토마토가 익지 않은 경우(visited에 False가 있는 경우)
    print(result)
else:
    print(-1)
