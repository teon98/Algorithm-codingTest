"""
탐색 범위가 2,000만을 넘어갈 때 고려해보기 
시간복잡도 O(logN)

TIP! 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 넓으므로 데이터의 개수가 1,000만 개를 넘어갈수 있다.
이럴 경우 input() 함수를 그냥 사용하면 동작 속도가 느려져 시간 초과로 오답 판정을 받을 수 있으니
입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다.
"""
import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid -1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

input= sys.stdin.readline

#입력 받은 문자열
print(input().split())