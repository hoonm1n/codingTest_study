import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)
dp = [[0,1] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(now):
    global tree, visited, dp
    visited[now] = 1
    dp[now][1] = 1

    for c in tree[now]:
        if visited[c] == 0:
            dfs(c)
            dp[now][0] += dp[c][1]
            dp[now][1] += min(dp[c][0], dp[c][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))