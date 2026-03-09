"""
문제: 숨박꼭질2
링크: https://www.acmicpc.net/problem/12851
난이도: 골드4
푼 날짜: 2025.05.12
"""
import sys
from collections import deque

def bfs(N,K):
    queue = deque([(N,0)])
    visited = [-1]*100001
    way = [0]*100001
    visited[N] = 0
    way[N] = 1

    while queue:
        x, time = queue.popleft()

        if x == K:
           print(time)
           print(way[x])
           break

        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= 100000:
                if visited[nx] == -1:
                    queue.append((nx, time+1))
                    visited[nx] = time+1
                    way[nx] = way[x] #x에서 nx로 가는 모든 경로는 x까지의 경로 수와 같음
                else:
                    if visited[nx] == time+1: #같은 타임이면
                        way[nx] += way[x] #같은 시간에 또 갈 수 있는 경우 누적

input = sys.stdin.readline

N, K = map(int, input().split()) #N: 수빈이의 위치, K: 동생의 위치
bfs(N, K)