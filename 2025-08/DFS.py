"""
graph [['A','B'], ['B','C'],['C','D'],['D','E']] 
start 'A'
return ['A','B','C','D','E']

graph [['A','B'], ['A','C'], ['B','D'],['B',E'],['C','F'],['E','F']]
start 'A'
return ['A','B','D','E','F','C']
"""
from collections import defaultdict

def dfs(v, graph, visited, result):
    visited.add(v)
    result.append(v)

    for node in graph.get(v, []):
        if node not in visited:
            dfs(node, graph, visited, result)
    

def solution(graph, start):
    # 그래프를 인접 리스트로 반환
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)
    
    visited = set()
    result = []
    dfs(start, adj_list, visited, result)
    print(result)


solution([['A','B'], ['B','C'],['C','D'],['D','E']] , 'A')
solution([['A','B'], ['A','C'], ['B','D'],['B','E'],['C','F'],['E','F']], 'A')