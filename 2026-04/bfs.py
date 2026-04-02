"""
BFS(Breath First Search)

큐 사용하기

"최소 몇 번",
"가장 빠른",
"최단 거리"
등, 처음 목적지에 도달하는 순간이 곧 최단 경로임이 보장되는 문제.

- 트리가 넓고 얇은 구조(각 노드가 자식 100개 등) -> DFS 유리
- 트리가 좁고 깊은 구조(긴체인) -> BFS 유리
"""
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9
bfs(graph, 1, visited)