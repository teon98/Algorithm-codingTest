"""
유기농 배추
https://www.acmicpc.net/problem/1012
실버2
"""

import sys
from collections import deque

#방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS 메서드 정의
def bfs(graph, cabbage_list, N, M):
    count = 0

    #첫번째 배추리스트 부터 시작
    for (a, b) in cabbage_list:

        if graph[a][b] == 0: 
            continue

        queue = deque([(a,b)])
        graph[a][b] = 0

        #큐가 빌 때까지 반복
        while queue:

            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위 벗어날 경우 무시
                if nx < 0 or ny < 0 or nx >= M or ny >= N:
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
T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)] 
    cabbage_list = []
    for j in range(K):
        x, y = map(int, input().split())
        cabbage_list.append((x,y))
        graph[x][y] = 1

    result = bfs(graph, cabbage_list, N, M)
    print(result)