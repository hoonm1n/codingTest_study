import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
mems = list(map(int,input().rstrip().split()))
costs = list(map(int,input().rstrip().split()))

dp = [[0] * (sum(costs)+1) for _ in range(n+1)]
result = sum(costs)+1

for i in range(1, n+1):
    memory = mems[i-1]
    cost = costs[i-1]
    for j in range(0, sum(costs)+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)

        if dp[i][j] >= m:
            result = min(result, j)

print(result)