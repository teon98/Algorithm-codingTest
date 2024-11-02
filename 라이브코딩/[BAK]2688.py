import sys
input = sys.stdin.readline

T = int(input())
total = 64
dp = [[1]*10 for _ in range(total)]

for i in range(1, total):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])
        
for j in range(T):
    temp = int(input())
    print(sum(dp[temp-1]))