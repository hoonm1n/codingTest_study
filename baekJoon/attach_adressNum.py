from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
map = [list(map(int, input())) for _ in range(n)]

house_cnt = 0
curr_cnt = 0
sizes = []
def DFS(x, y):
    global curr_cnt
    if 0>x or x>=n:
        return 
    if 0>y or y>=n:
        return
    if map[x][y] == 0:
        return
    map[x][y] = 0
    curr_cnt += 1
    for i in range(4):
        DFS(x+dx[i], y+dy[i])

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            curr_cnt = 0
            DFS(i,j)
            house_cnt += 1
            sizes.append(curr_cnt)

print(house_cnt)
sizes.sort()
for size in sizes:
    print(size)
