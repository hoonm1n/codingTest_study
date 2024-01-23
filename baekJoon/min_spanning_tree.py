import sys
input = sys.stdin.readline

def find(root, x):
    if root[x] != x:
        root[x] = find(root ,root[x])
    return root[x]

def union(root, x, y):
    x = find(root, x)
    y = find(root, y)
    if x < y:
        root[y] = x
    else:
        root[x] = y


V, E = map(int, input().split())
edges = []
for i in range(E):
    edges.append(list(map(int, input().split())))

root = dict()
for i in range(1, V+1):
    root[i] = i

edges = sorted(edges, key=lambda x: x[2])

result = 0
for edge in edges:
    s, e, w = edge
    if find(root, s) != find(root, e):
        union(root, s, e)
        result += w

print(result)



