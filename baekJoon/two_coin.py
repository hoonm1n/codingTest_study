n, m = map(int,input().split())

board = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

coins = []
result = 1e9
for i in range(n):
    for j in range(m):
        if board[i][j] == "o":
            coins.append((i,j))

def check(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return True
    return False

def DFS(x,y,a,b,cnt):
    global result
    if cnt > 10:
        return
    if (check(x,y) and not check(a,b)) or (not check(x,y) and check(a,b)):
        result = min(result, cnt)
        return
    visited[x][y] = 1
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        next_a = a + dx[i]
        next_b = b + dy[i]
        if check(next_x, next_y) and check(next_a, next_b):
            continue
        if 0 <= next_x < n and 0 <= next_y < m:
            if board[next_x][next_y] == "#":
                next_x = x
                next_y = y
        if 0 <= next_a < n and 0 <= next_b < m:
            if board[next_a][next_b] == "#":
                next_a = a
                next_b = b
        # if visited[next_x][next_y] == 0:
        DFS(next_x, next_y,next_a,next_b, cnt + 1)

DFS(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)
if result == 1e9:
    print(-1)
else:
    print(result)
    
