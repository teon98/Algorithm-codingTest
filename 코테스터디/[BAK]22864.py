'''
* Author    : 강태영
* Date      : 2024.10.29(TUE)
* Runtime   : 
* Memory    : 
* Algorithm : 구현

https://www.acmicpc.net/problem/22864
시각(브론즈2)
'''

import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())

tired = 0
time = 1
work = 0
while time < 24:

    if tired <= M:
        work += B
        tired += A
    else:
        tired -= C
        if tired < 0:
            tired = 0

    print("시간", time)
    print("피로도", tired)

    time += 1 

# print(tired)
# print(time)
print(work)