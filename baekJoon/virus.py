n = int(input())
k = int(input())

network = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(k):
    a, b = map(int,input().split())
    network[a].append(b)
    network[b].append(a)

result = 0
def DFS(x):
    global result
    visited[x] = 1
    result += 1
    for i in network[x]:
        if visited[i] == 0:
            DFS(i)


DFS(1)
print(result - 1)