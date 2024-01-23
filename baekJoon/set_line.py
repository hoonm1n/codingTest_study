import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())

entries_num = [0] * (N+1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    entries_num[a] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, N+1):
        if entries_num[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for k in graph[now]:
            entries_num[k] -= 1
            if entries_num[k] == 0:
                q.append(k)

    return result
result = topology_sort()
result.reverse()

print(*result)