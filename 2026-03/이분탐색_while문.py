"""
코테에서는 대부분 while 방식을 쓴다

이유
1. 재귀 호출 비용 없음
2. 파이썬 재귀 제한 문제 없음
3. 디버깅 쉬움
4. *파라메트릭 서치 구현이 편함 
*파라메트릭 서치: 어떤 값이 가능한지(조건을 만족하는지)를 기준으로 정답을 찾는 이분 탐색 방식
"""
def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start + end) //2

        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return