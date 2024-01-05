def dfs(i,j):
    if n<=i or i<0 or j<0 or m<=j:
        return False
    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        return True
    return False


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
visited = [[False]*m for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)

