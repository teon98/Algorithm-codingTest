"""
문제: 벽 부수고 이동하기
링크: https://www.acmicpc.net/problem/2206
난이도: 골드3
푼 날짜: 2025.05.19

visited를 3차원으로 구성
"""
import sys
from collections import deque
import copy

def bfs(graph, visited, N, M):
    queue = deque([(0,0,0)]) # 시작은 0,0부터 
    visited[0][0][0] = 1 #시작은 거리 1

    while queue:
        x,y,broken = queue.popleft() 

        if x == (N-1) and y == (M-1):
            return visited[x][y][broken]

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #갈 수 없는 경로는 무시
            if nx < 0 or ny < 0 or nx >=N or ny >=M:
                continue
            
            #이동할 수 있는 경우
            if graph[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                visited[nx][ny][broken] = visited[x][y][broken] + 1 #거리 증가
                queue.append((nx,ny,broken))
            
            #벽을 부수지 않았고, 다음 칸이 벽인 경우 -> 부수고 이동
            elif graph[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                visited[nx][ny][1] = visited[x][y][broken] + 1
                queue.append((nx, ny, 1))
        
        #print(queue)
    
    return -1


input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    line = list(map(int,input().strip()))
    graph.append(line)

"""
GPT 솔루션: 3차원 visited 배열을 활용하자
visited[x][y][0] = 벽을 안 부수고 (0) 도착한 최단 거리
visited[x][y][1] = 벽을 부수고 (1) 도착한 최단 거리
"""
visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]

#print(visited)
result = bfs(graph, visited, N, M)
print(result)