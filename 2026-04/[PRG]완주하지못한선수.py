'''
* Date      : 2026.04.03
* Algorithm : 해시

https://school.programmers.co.kr/learn/courses/30/lessons/42576
'''
def solution(participant, completion):
    answer = ''
    
    temp = dict()
    
    for name in participant:
        if name in temp:
            temp[name] += 1
        else:
            temp[name] = 1
    
    for name2 in completion:
        temp[name2] -= 1
    
    for name3 in temp.keys():
        if temp[name3] == 1:
            answer = name3
            break
            
    return answer