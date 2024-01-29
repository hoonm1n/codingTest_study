import sys
from collections import deque
input = sys.stdin.readline

n, m, v= map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
queue = deque()

for i in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

def DFS(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            DFS(i)

def BFS(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1,n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            queue.append(i)
            visited[i] = 1
    while queue:
        next = queue.popleft()
        print(next, end=' ')
        for i in range(1,n+1):
            if visited[i] == 0 and graph[next][i] == 1:
                queue.append(i)
                visited[i] = 1

DFS(v)
print()
visited = [0]*(n+1)
BFS(v)
    


