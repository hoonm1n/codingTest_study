import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split())

graph = [[0]*m for _ in range(n)]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
visted = [[0]*m for _ in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

result = 0
cnt = 0
def DFS(x,y):
    global result, cnt
    visted[x][y] = 1
    if graph[x][y] == 0:
        return
    cnt += 1
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m and visted[next_x][next_y] == 0:
            DFS(next_x,next_y)

    result = max(result, cnt)

for i in range(n):
    for j in range(m):
        if visted[i][j] == 0:
            cnt = 0
            DFS(i,j)

print(result)