'''
게임 개발
https://www.acmicpc.net/problem/1516
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
time = [0]*(N+1)
indegree = [0]*(N+1)
graph = [[] for i in range(N+1)]

for i in range(N):
    temp = list(map(int, input().split()))[:-1]
    time[i+1] = temp[0]
    graph[i+1] = temp[1:]

    for j in graph[i+1]:
        indegree[i] += 1

print(time)
print(indegree)
print(graph)