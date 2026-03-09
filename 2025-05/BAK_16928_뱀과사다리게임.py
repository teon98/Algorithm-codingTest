"""
문제: 뱀과 사다리 게임
링크: https://www.acmicpc.net/problem/16928
난이도: 골드5
푼 날짜: 2025.05.12

3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17

3
"""
import sys
from collections import deque

def bfs(visited, ladder_list, snake_list):
    queue = deque([(1,0)])
    visited[1] = True #시작은 1번 칸

    while queue:
        x, t = queue.popleft()

        if x == 100:
            print(t)
            break
        
        for i in range(1,7):
            nx = x+i

            if nx > 100 :
                continue
            
            # 사다리일 때 목적지로 점프
            for ls, le in ladder_list:
                if ls == nx:
                    nx = le
                    break
                
            for ss, se in snake_list:
                if ss == nx:
                    nx = se
                    break

            if visited[nx] == False:
                queue.append((nx, t+1))
                visited[nx] = True
    
        #print(queue)


input = sys.stdin.readline

visited = [False for _ in range(101)]

N, M = map(int, input().split()) #N: 사다리수 / M: 뱀의 수
ladder_list = []
for _ in range(N):
    a, b = map(int, input().split())
    ladder_list.append((a,b))

snake_list = []
for _ in range(M):
    a, b = map(int, input().split())
    snake_list.append((a,b))

bfs(visited, ladder_list, snake_list)