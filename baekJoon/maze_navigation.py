from collections import deque
INF = 1e9

n, m = map(int, input().split())
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

map = [list(map(int, input())) for _ in range(n)]
visited = [[INF]*m for _ in range(n)]
q = deque()

def BFS(x, y):
    q.append((x,y))
    visited[x][y] = 1
    while q:
        curr = q.popleft()
        for i in range(4):
            next_x = curr[0] + dx[i]
            next_y = curr[1] + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if map[next_x][next_y] == 1 and visited[next_x][next_y] == INF:
                    q.append((next_x,next_y))
                    visited[next_x][next_y] = min(visited[curr[0]][curr[1]] + 1, visited[next_x][next_y])
                    
BFS(0,0)
print(visited[-1][-1])