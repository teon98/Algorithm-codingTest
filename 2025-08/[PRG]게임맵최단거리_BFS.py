"""
LINK: https://school.programmers.co.kr/learn/courses/30/lessons/43163
DATE: 2025.08.09
"""

from collections import deque
def bfs(start, maps, N, M):
    queue = deque([start])
    
    #방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        if x == N-1 and y == M-1: #끝에 도달했을 때
            return maps[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 이상일 경우 넘어가기
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if maps[nx][ny] == 1:
                #방문처리
                maps[nx][ny] = maps[x][y] + 1
                #큐에 넣기
                queue.append((nx, ny))
    
    return -1
    
    # 도달 할 수 없는 경우에는 -1 반환

#갈 수 없는 길: 0, 갈 수 있는 길: 1
def solution(maps):
    
    N = len(maps)
    M = len(maps[0])
    
    start = (0,0)
    
    answer = bfs(start, maps, N, M)
    
    return answer