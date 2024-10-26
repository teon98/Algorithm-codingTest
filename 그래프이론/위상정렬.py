'''
위상 정렬 알고리즘
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 아래 과정을 반복한다.
  1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프ㅔ서 제거한다.
  2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
※ 위상 정렬 문제에서는 사이클이 발생하지 않는다고 명시하는 경우가 많다.
'''
import sys
input = sys.stdin.readline
from collections import deque


#노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(v+1) #[0, 0, 0, 0, 0, 0, 0, 0]
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프)초기화
graph = [[] for i in range(v+1)] #[[], [], [], [], [], [], [], []]


#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b) #정점 A에서 B로 이동 가능
  #진입차수를 1 증가
  indegree[b] += 1

#indegree : [0, 0, 1, 1, 2, 1, 2, 1]
#graph: [[], [2, 5], [3, 6], [4], [7], [6], [4], []]

#위상 정렬 함수
def topology_sort():
  result = [] #알고리즘 수행 결과를 담을 리스트
  q = deque() #큐 기능을 위한 deque 라이브러리 사용

  #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  
  print("result", result)
    
  #큐가 빌 때까지 반복
  while q:
    #큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    print("now", now)
    #해당 원소와 연결된 노드를 진입차수에서 1빼기
    for i in graph[now]:
      indegree[i] -= 1
      #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
    print(indegree)
    print(graph)

  #위상 정렬을 수행한 결과 출력
  for i in result:
    print(i, end=' ')
topology_sort()
