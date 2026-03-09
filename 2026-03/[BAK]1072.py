'''
* Date      : 2026.03.09
* Algorithm : 이진탐색(문제가 거지 같아요)

https://www.acmicpc.net/problem/1072
게임(실버3)
'''
import math
def Z_calculator(X, Y):
    return (Y*100) // X

def binary_Z_search(start, end, X, Y, Z, t):
    if start > end :
        return Z, t
    
    mid = (start + end) // 2
    new_Z = Z_calculator(X + mid, Y + mid)

    if new_Z > Z:
        return binary_Z_search(start, mid - 1, X, Y, Z, mid)
    else:
        return binary_Z_search(mid + 1, end, X, Y, Z, t)

X, Y = map(int, input().split())
Z = Z_calculator(X, Y)

final_Z, result = binary_Z_search(1, 10**9, X, Y, Z , -1)

if final_Z >= 99:
    print(-1)
else:
    print(result)