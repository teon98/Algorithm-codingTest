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
