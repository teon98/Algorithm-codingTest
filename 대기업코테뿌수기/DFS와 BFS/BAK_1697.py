"""
문제: 숨바꼭질
링크: https://www.acmicpc.net/problem/1697
난이도: 실버1
푼 날짜: 2025.05.07
"""

import sys
from collections import deque

def bfs(N,K):
    queue = deque([(N,0)])
    visited = set()
    visited.add(N)
    
    while queue:
        x, time = queue.popleft()

        if x == K:
            return time
        
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= 100000 and nx not in visited:
                queue.append((nx, time+1))
                visited.add(nx)

input = sys.stdin.readline

#N: 수빈이의 위치, K: 동생의 위치
N, K = map(int, input().split())
print(bfs(N,K))