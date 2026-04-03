'''
* Date      : 2026.04.03
* Algorithm : 해시

https://school.programmers.co.kr/learn/courses/30/lessons/43163
'''
from collections import deque

def compare_count(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt
    
def solution(begin, target, words):
    visited = {}
    for word in words:
        visited[word] = False
    
    def bfs(start):
        queue = deque([(start, 1)])
        visited[start] = True
        
        while queue:
            n, cnt = queue.popleft()
            print(n, cnt)
            
            if n == target:
                return cnt
            
            for word in words:
                if visited[word]:
                    continue
                    
                if compare_count(n, word) == 1:
                    queue.append((word, cnt+1))
                    visited[word] = True
        return 0
        
    # words에서 시작점 찾기
    start = ''
    for word in words:
        if compare_count(begin, word) == 1:
            start = word
            break    
    answer = bfs(start)
    
    return answer