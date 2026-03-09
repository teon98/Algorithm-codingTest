"""
LINK: https://school.programmers.co.kr/learn/courses/30/lessons/43163
DATE: 2025.08.09
"""

from collections import deque

def bfs(start, target, words, visited, N):

    queue = deque(start)
    
    while queue:
        d, i, w = queue.popleft() # d: depth
        print(d, i, w)
        
        if w == target:
            print (d, w)
            return d
        
        for index, word in enumerate(words):
            
            if visited[index] == True: #이미 방문한 친구면 넘어가기
                continue
            
            cnt1 = 0
            for i in range(N): 
                if w[i] != word[i]:
                    cnt1 += 1

            cnt2 = 0
            if cnt1 == 1: #한글 자만 바뀌었다면
                for j in range(N):
                    if word[j] == target[j]: # target 값에 포함되는 글자가 있는지 
                        cnt2 += 1

            if cnt2 > 0:
                queue.append((d+1, index, word))
                visited[index] = True #시작 word 방문처리
    return 0

def solution(begin, target, words):
    N = len(begin)
    start = []
    
    visited = [False for _ in range(len(words))]
    
    # words 중 먼저 시작할 수 있는 단어 찾기
    for index, word in enumerate(words):
        cnt1 = 0
        for i in range(N): 
            if begin[i] != word[i]:
                cnt1 += 1
        
        cnt2 = 0
        if cnt1 == 1: #한글 자만 바뀌었다면
            for j in range(N):
                if word[j] == target[j]: # target 값에 포함되는 글자가 있는지 
                    cnt2 += 1
        
        if cnt2 > 0:
            start.append((1,index,word)) #0:depth
            visited[index] = True
    
    result = bfs(start, target, words, visited, N)
    
    return result