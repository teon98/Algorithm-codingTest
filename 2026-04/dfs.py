"""
DFS (Depth-First-Search) 

stack 사용하기

"경로가 존재하는지", 
"연결되어 있는지",
"모든 경우의 수",
"조합",
"백트래킹"
등
모든 가능성을 끝까지 파고들어야 하는 문제들에 사용.

- 트리가 넓고 얇은 구조(각 노드가 자식 100개 등) -> DFS 유리
- 트리가 좁고 깊은 구조(긴체인) -> BFS 유리
"""
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)
            
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)