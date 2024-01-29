#BFS를 이용해 풀기
from collections import deque

def solution(numbers, target):
    row = [0]
    for num in numbers:
        result = []
        queue = deque(row)
        while queue:
            v = queue.popleft()
            result.append(v+num)
            result.append(v-num)
        row = result
        #print(row)
    return row.count(target)


"""
print(row)
[4, -4]
[5, 3, -3, -5]
[7, 3, 5, 1, -1, -5, -3, -7]
[8, 6, 4, 2, 6, 4, 2, 0, 0, -2, -4, -6, -2, -4, -6, -8]
"""