"""
문제: 안전영역
링크: https://www.acmicpc.net/problem/2468
난이도: 실버1
푼 날짜: 2025.05.07
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

5
direction = [(-1,0), (0,1), (1,0), (0,-1)]
"""
import sys
from collections import deque
import copy

def bfs(graph, start, N):
    queue = deque([start])
    graph[start[0]][start[1]] = True

    #방향 정의(상,하,좌,우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            # 범위 벗어날 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 이동 가능 할 경우
            if graph[nx][ny] == False:
                queue.append((nx,ny))
                graph[nx][ny] = True


input = sys.stdin.readline

N = int(input())
graph = []

for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

#temp_graph = copy.deepcopy(graph)

# # 가장 낮은 높이랑 가장 높은 높이를 구한다 -> 틀림
# min_val = min([min(row) for row in graph])
# max_val = max([max(row) for row in graph])

# ⚠️ 비가 안올 수도 있다는 조건을 고려해야함
max_val = max([max(row) for row in graph])

result = []
for standard in range(max_val+1):
    #새로 돌때마다 새로운 graph 초기화 해야함
    temp_graph = copy.deepcopy(graph) #기존에 만든 graph를 깊은 복사로 가져와야한다
    #문제 단순화하기 지나갈수 있는 영역(Visited False), 지나갈 수 없는 영역(Visited True)
    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] > standard:
                temp_graph[i][j] = False
            else:
                temp_graph[i][j] = True

    # False인 친구를 찾아서 BFS 타고 몇 번 타는지 세기
    count = 0
    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] == False:
                start = (i, j)
                bfs(temp_graph, start, N)
                count += 1

    result.append(count)

print(max(result))
