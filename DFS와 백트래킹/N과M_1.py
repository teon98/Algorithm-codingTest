"""
문   제: https://www.acmicpc.net/problem/15649
푼 날짜: 2025.08.07
유형: 백트래킹, DFS
"""
import sys

def back(depth, arr, N, M):
    if depth == M:
        print(*arr)
        return 
    for i in range(1, N+1):
        # 중복 확인
        if i not in arr:
            arr.append(i)
            back(depth+1, arr, N, M)
            arr.pop() #상태복원

input = sys.stdin.readline
N, M = map(int, input().split())
back(0, [], N, M)
