import sys
input = sys.stdin.readline

# DFS 탐색 방향: 오른쪽 위, 오른쪽, 오른쪽 아래
directions = [(-1, 1), (0, 1), (1, 1)]  # (행 이동, 열 이동)

def dfs(x, y):
    # 현재 위치에서 오른쪽으로 파이프 설치를 시도
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        # 다음 위치가 격자 내부이고, 빈 칸이면 이동
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.':
            grid[nx][ny] = 'x'  # 방문 처리 (파이프 설치)
            
            # 가스관(마지막 열)에 도달하면 성공
            if ny == C - 1:
                return True
            
            # 다음 위치에서 DFS 진행
            if dfs(nx, ny):
                return True
    
    # 더 이상 진행할 수 없으면 False 반환
    return False

# 입력 처리
R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

result = 0  # 성공적으로 설치한 파이프라인 수

# 각 행에서 파이프라인 설치 시도
for i in range(R):
    if dfs(i, 0):  # 첫 번째 열에서 DFS 시작
        result += 1

# 결과 출력
print(result)
