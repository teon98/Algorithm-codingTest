N = int(input())

# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + array[i])
    #print(i, d)

print(d[N-1])