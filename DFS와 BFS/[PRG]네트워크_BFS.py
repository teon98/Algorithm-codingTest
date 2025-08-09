"""
LINK: https://school.programmers.co.kr/learn/courses/30/lessons/43162
DATE: 2025.08.09
"""

from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return 1
    
def solution(n, computers):
    answer = 0
    
    # 인접 리스트로 먼저 표현하기
    graph = [[] for i in range(n+1)]
    
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if computers[i][j] == 1:
                graph[i+1].append(j+1)
    
    visited = [False for i in range(n+1)]
    visited[0] = True
    
    result = 0
    
    for i in range(1, len(visited)):
        if not visited[i]:
            result += bfs(i, graph, visited)
    
    return result