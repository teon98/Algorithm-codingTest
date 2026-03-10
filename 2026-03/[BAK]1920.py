'''
* Date      : 2026.03.10
* Title     : 수 찾기
* Algorithm : 이진탐색
* Level     : 실버4

https://www.acmicpc.net/problem/1920
'''
def binary_search(target, data):
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start + end)//2
        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    
    return 0

N = int(input())
data = list(map(int, input().split()))
data_sort = sorted(data)

M = int(input())
target_list = list(map(int, input().split()))

for target in target_list:
    result = binary_search(target, data_sort)
    print(result)