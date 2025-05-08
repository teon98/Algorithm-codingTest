"""
문제: 트리의 부모 찾기
링크: https://www.acmicpc.net/problem/11725
난이도: 실버2
푼 날짜: 2025.05.07

7
1 6
6 3
3 5
4 1
2 4
4 7

4
6
1
3
1
4

"""
import sys
from collections import deque

def bfs(linked_list, visited, graph):
    #0번째는 무시한다
    visited[0] = True

    #트리의 루트는 1
    queue = deque([1])
    visited[1] = True

    while queue:
        
        v = queue.popleft()
        
        for i in linked_list[v]:
            if not visited[i]:
                graph[i] = v
                visited[i] = True
                queue.append(i)
    
    return graph[2:]


input = sys.stdin.readline

N = int(input())

linked_list = [[]*i for i in range(N+1)]
visited =[False for _ in range(N+1)]
graph = [0 for _ in range(N+1)]

for _ in range(N-1):
    k, v = map(int, input().split())
    linked_list[k].append(v)
    linked_list[v].append(k)

result = bfs(linked_list, visited, graph)

for r in result:
    print(r)
