n = int(input())
passengers = list(map(int,input().split()))
passengers.insert(0, 0)
k = int(input())
dp = [[0]*(n+1) for _ in range(4)]

for i in range(1,4):
    for j in range(k*i, n+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + sum(passengers[j-k+1: j+1]))

print(dp[3][n])