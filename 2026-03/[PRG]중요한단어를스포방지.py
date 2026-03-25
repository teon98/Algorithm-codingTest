def find_word_range(message, index):
    start = index
    end = index
    
    while start>=0 :
        if start == 0 :
            break
        elif message[start] == " ":
            start += 1
            break
        start -= 1
    
    while end<=len(message)-1 :
        if end == len(message)-1:
            break
        elif message[end] == " ":
            end -= 1
            break
        end += 1
    
    return (start, end)
    
def solution(message, spoiler_ranges):
    answer = 0
    
    split_message_list = list(message.split()) # ['hello', 'world', 'hello']
    
    temp = set()
    for i in range(len(message)):
        if message[i] == " ":
            continue
        result = find_word_range(message, i)
        temp.add(result)
    
    message_word_ranges = sorted(list(temp)) # [(0,4), (6,10), (12,16)]
    
    #print(split_message_list)
    #print(message_word_ranges)
    
    # spoiler 단어 완성 범위 찾기
    temp2 = set()
    for i in range(len(message)):
        if message[i] == " ":
            continue
        for start, end in spoiler_ranges:
            if i>=start and i<=end:
                result = find_word_range(message, i)
                temp2.add(result)
                break
    
    spoiler_complete_ranges = sorted(list(temp2))
    #print(spoiler_complete_ranges) # [(0, 4), (6, 10)]
    
    # spoiler 단어 아닌 범위 찾기
    not_spoiler_word_ranges = []
    for word_range in message_word_ranges:
        if word_range not in spoiler_complete_ranges:
            not_spoiler_word_ranges.append(word_range)
    
    #print(not_spoiler_word_ranges) # [(12, 16)]
    
    answer_list = []
    
    for i in range(len(message_word_ranges)):
        if (message_word_ranges[i] in spoiler_complete_ranges):
            if split_message_list[i] not in answer_list:
                answer_list.append(split_message_list[i]) #일단 후보 추가
            for j in range(len(not_spoiler_word_ranges)): 
                a, b = not_spoiler_word_ranges[j]
                if message[a:b+1] == split_message_list[i]: # 스포일러가 아닌 범위에있는 단어와 같은 단어가 있는가
                    answer_list.remove(split_message_list[i]) # 그럼 삭제 
                    break
        
    #print(answer_list)
    answer = len(answer_list)
    return answer