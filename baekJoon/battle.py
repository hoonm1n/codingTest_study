import sys
from collections import deque
# input = sys.stdin.readline

m, n = map(int, input().split())

map = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
q = deque()

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

white = 0
blue = 0

def BFS(x, y):
    q.append((x,y))
    color = map[x][y]
    visited[x][y] = 1
    cnt = 1
    while q:
        curr = q.popleft()
        for i in range(4):
            next_x = curr[0] + dx[i]
            next_y = curr[1] + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if color == map[next_x][next_y] and visited[next_x][next_y] == 0:
                    q.append((next_x,next_y))
                    visited[next_x][next_y] = 1
                    cnt += 1
    
    return color, cnt

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            color, cnt = BFS(i, j)
            if color == "W":
                white += cnt**2
            else:
                blue += cnt**2

print(white, blue)

