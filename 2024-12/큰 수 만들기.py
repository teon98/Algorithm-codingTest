def solution(number, k):
    answer = ''
    
    #stack 생성
    stack = []
    
    for num in number:
        #스택에 값이 있고, 제거 횟수가 남아 있으며, 현재 숫자가 스택 마지막보다 크면 제거
        while stack and k>0 and stack[-1] < num:
            stack.pop()
            k-=1
        stack.append(num)
    
    #아직 제거해야 할 숫자가 남아 있으면 뒤에서 자르기
    if k>0:
        stack = stack[:-k]
        
    #스택의 숫자들을 합쳐서 결과 반환
    return ''.join(stack)