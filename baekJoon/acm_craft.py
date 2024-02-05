import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
result = []

for _ in range(T):
    n, k = map(int, input().rstrip().split())
    delay = list(map(int,input().rstrip().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(k):
        a, b = map(int,input().rstrip().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())
    dp = [0] * (n+1)

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = delay[i-1]

    while q:
        now = q.popleft()

        for g in graph[now]:
            dp[g] = max(dp[g], dp[now] + delay[g-1])
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)

    result.append(dp[w])
 
for i in range(T):
    print(result[i])
