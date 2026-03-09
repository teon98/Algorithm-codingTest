"""
문제: 탈출
링크: https://www.acmicpc.net/problem/3055
난이도: 골드4
푼 날짜: 2025.05.12

.:비어있는 곳, *:물이 차있는 곳, X:돌, D:비버의 굴, S:고슴도치의 위치

- 고슴도치: 인접한 네 칸 중 하나로 이동
- 물: 매 분마다 비어있는 칸으로 확장
- 물과 고슴도치 -> 돌 통과 x
- 고슴도치 -> 물로 차있는 구역 이동 x
- 물 -> 비버의 소굴로 이동 X
- 고슴도치 -> 물이 찰 예정인 칸으로 이동 X

목적: 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간

3 3
D.*
...
.S.

3
"""
import sys
from collections import deque

def water_bfs(graph, water_start, R, C):
    water_map = [[-1 for _ in range(C)] for _ in range(R)]
    queue = deque([])

    for i,j,t in water_start:
        queue.append((i,j,t))
        water_map[i][j] = t
    
    while queue:
        x,y,t = queue.popleft()

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx<0 or ny<0 or nx>=R or ny>=C:
                continue

            if water_map[nx][ny] == -1 and graph[nx][ny] != 'X' and graph[nx][ny] != 'D': #물도 비버의 굴로 찰 수 없다
                water_map[nx][ny] = t+1
                queue.append((nx,ny,t+1))

    return water_map

def bfs(graph, visited, water_map, S_start, R, C):
    queue = deque([S_start])
    visited[S_start[0]][S_start[1]] = True

    while queue:
        x, y, t = queue.popleft()

        if graph[x][y] == 'D': #비버의 집에 방문했을 때
            print(t)
            return

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx<0 or ny<0 or nx>=R or ny>=C:
                continue

            if visited[nx][ny] == False and (water_map[nx][ny] == -1 or water_map[nx][ny] > t+1): #물에 잠기지 않거나 방문하지 않았을 때
                queue.append((nx, ny, t+1))
                visited[nx][ny] = True
        #print(queue)
    print("KAKTUS")

input = sys.stdin.readline

R, C = map(int, input().split())

graph = []
visited = [[False for _ in range(C)] for _ in range(R)]
for _ in range(R):
    graph_line = list(input().strip())
    graph.append(graph_line)

#print(visited)
#print(graph)

S_start = ()
water_start = []
#비버, 물, 고슴도치의 위치 찾기
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            S_start = (i,j,0)
        elif graph[i][j] == '*':
            water_start.append((i,j,0))
        elif graph[i][j] == 'X':
            visited[i][j] = True

# 물이 빈 칸에 언제 도착하는지 그래프 그리기
water_map = water_bfs(graph, water_start, R, C)
#print(water_map)

#고슴도치 -> 비버 BFS
bfs(graph, visited, water_map, S_start, R, C)