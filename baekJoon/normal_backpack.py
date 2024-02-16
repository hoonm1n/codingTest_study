import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
values = []
weights = []
for i in range(n):
    a, b = map(int, input().rstrip().split())
    weights.append(a)
    values.append(b)

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight = weights[i-1]
    value = values[i-1]
    for j in range(0, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(max(dp[n]))