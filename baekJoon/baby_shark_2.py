import sys
from collections import deque

n, m = map(int,input().split())
space = []
for _ in range(n):
    space.append(list(map(int,input().split())))

vistied = [[0]*m for _ in range(n)]
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

result = 0

def bfs(x,y):
    global vistied, result
    q = deque()
    q.append((x,y,0))
    vistied[x][y] = 1
    while q:
        now = q.popleft()
        if space[now[0]][now[1]] == 1:
            result = max(result, now[2])
            break
        for i in range(8):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if vistied[nx][ny] == 0:
                    q.append((nx,ny,now[2]+1))
                    vistied[nx][ny] = 1
        

for i in range(n):
    for j in range(m):
        vistied = [[0]*m for _ in range(n)]
        if space[i][j] == 0:
            bfs(i,j)

print(result)

