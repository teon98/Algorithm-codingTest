#DFS로 풀기
cnt = 0

def dfs(numbers, v, sum, target):
    global cnt
    if len(numbers) == v:
        if sum == target:
            cnt += 1
        return
            
    dfs(numbers, v+1, sum+numbers[v], target)
    dfs(numbers, v+1, sum-numbers[v], target)
    
def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    return cnt