'''
* Date      : 2026.04.02
* Algorithm : DFS

https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''
cnt = 0 # 전역변수

def dfs(result, numbers, target, idx):
    global cnt
    if idx == len(numbers): #마지막까지 왔을 때
        if result == target: #합한 값이 target이랑 같으면
            cnt += 1 # 카운트
        return 
    dfs(result + numbers[idx], numbers, target, idx+1)
    dfs(result - numbers[idx], numbers, target, idx+1)

def solution(numbers, target):
    answer = 0

    dfs(0, numbers, target, 0)
    
    return cnt