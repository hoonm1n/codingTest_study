n = int(input())

jump = [list(map(int,input().split())) for _ in range(n)]
table = [[0]*n for _ in range(n)]
table[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        l = jump[i][j]
        if i+l < n:
            table[i+l][j] += table[i][j]
        if j+l < n:
            table[i][j+l] += table[i][j]

print(table[-1][-1])