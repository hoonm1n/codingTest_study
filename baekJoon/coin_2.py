INF = 1e9

n, k = map(int, input().split())

table = [INF] * (k+1)
table[0] = 0
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

for c in coins:
    for i in range(c, k+1):
        curr = table[i-c] + 1
        table[i] = min(curr, table[i])

if table[k] == INF:
    print(-1)
else:
    print(table[k])
