def solution(n, costs):
    answer = 0
    
    #가중치 기준으로 정렬
    costs.sort(key=lambda x:x[2])
    
    #시작 연결 점 찾기(사이클을 막기 위해)
    link = set([costs[0][0]]) # 첫 번째 간선의 시작 노드를 집합으로 저장 {0}
    
    while len(link) !=n : #set 안에 연결된 모든 위치가 연결되기전까지 실행
        for v in costs:
            if v[0] in link and v[1] in link:
                continue #set안에 정보가 있으면 넘어감
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]])
                print(link)
                answer += v[2]
                break
    
    print(link)
    return answer