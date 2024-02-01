n, s, m = map(int, input().split())
volume = list(map(int, input().split()))

table = [[0] * (m+1) for _ in range(n+1)]
table[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if table[i][j] == 1:
            if j + volume[i] <= m:
                table[i+1][j + volume[i]] = 1
            if j - volume[i] >= 0:
                table[i+1][j - volume[i]] = 1


if sum(table[n]) == 0:
    print(-1)
else:
    for i in range(m,-1,-1):
        if table[n][i] == 1:
            print(i)
            break


