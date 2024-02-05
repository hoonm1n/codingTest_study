INF = 1e9

n = int(input())
table = [INF] * n
table[0] = 0
pos = [0] * n
pos[0] = 1

street = list(input())

for i in range(n):
    if pos[i] == 0:
        continue
    curr = street[i]
    if curr == "B":
        for j in range(i,n):
            if street[j] == "O":
                pos[j] = 1
                table[j] = min(table[j], table[i] + (j-i)**2)
    elif curr == "O":
        for j in range(i,n):
            if street[j] == "J":
                pos[j] = 1
                table[j] = min(table[j], table[i] + (j-i)**2)
    else:
        for j in range(i,n):
            if street[j] == "B":
                pos[j] = 1
                table[j] = min(table[j], table[i] + (j-i)**2)

if table[-1] == INF:
    print(-1)
else:
    print(table[-1])
