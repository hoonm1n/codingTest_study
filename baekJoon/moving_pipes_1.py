N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

result = 0
def DFS(x, y, state):
    global result
    if x == N-1 and y == N-1:
        result += 1
        return

    if state == 0:
        if y == N - 1: 
            return

        if 0 <= x < N and 0 <= y + 1 < N and map[x][y + 1] == 0:
            DFS(x, y + 1, 0)

        if 0 <= x + 1 < N and 0 <= y + 1 < N and map[x][y + 1] == 0 and map[x + 1][y] == 0 and map[x + 1][
            y + 1] == 0:
            DFS(x + 1, y + 1, 2)

    elif state == 1:
        if x == N - 1: 
            return

        if 0 <= x + 1 < N and 0 <= y < N and map[x + 1][y] == 0:
            DFS(x + 1, y, 1)

        if 0 <= x + 1 < N and 0 <= y + 1 < N and map[x][y + 1] == 0 and map[x + 1][y] == 0 and map[x + 1][
            y + 1] == 0:
            DFS(x + 1, y + 1, 2)

    elif state == 2:
        if 0 <= x < N and 0 <= y + 1 < N and map[x][y + 1] == 0:
            DFS(x, y + 1, 0)

        if 0 <= x + 1 < N and 0 <= y < N and map[x + 1][y] == 0:
            DFS(x + 1, y, 1)

        if 0 <= x + 1 < N and 0 <= y + 1 < N and map[x][y + 1] == 0 and map[x + 1][y] == 0 and map[x + 1][
            y + 1] == 0:
            DFS(x + 1, y + 1, 2)



DFS(0,1,0)

print(result)
