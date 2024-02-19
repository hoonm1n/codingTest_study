import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().rstrip().split()))

answer = data[-1]
dp = [[0]*21 for _ in range(n)]

dp[0][data[0]] = 1

for i in range(1, n):
    for j in range(21):
        if j + data[i] <= 20:
            if j - data[i] >= 0:
                dp[i][j] = dp[i-1][j+data[i]] + dp[i-1][j-data[i]]
            else:
                dp[i][j] = dp[i-1][j+data[i]]
        elif j - data[i] >= 0:
            dp[i][j] = dp[i-1][j-data[i]]


print(dp[n-2][answer])