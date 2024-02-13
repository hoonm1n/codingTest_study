import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
citizens = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(n+1)]
for _ in range(1, n):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0,0] for _ in range(n+1)]
vistied = [0] * (n+1)

def dfs(start, p):
    vistied[start] = 1
    dp[start][1] += citizens[start-1]

    for e in graph[start]:
        if vistied[e] == 0:
            dfs(e, start)

    for e in graph[start]:
        if e != p:
            dp[start][0] += max(dp[e][0], dp[e][1])
            dp[start][1] += dp[e][0]

dfs(1, 0)
print(max(dp[1][0], dp[1][1]))