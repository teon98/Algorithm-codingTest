def binary_search(data, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binary_search(data, target, start, mid-1)
    else:
        return binary_search(data, target, mid + 1, end)
    

def solution(target, data):
    data.sort()
    start = 0
    end = len(data) - 1
    return binary_search(data, target, start, end)