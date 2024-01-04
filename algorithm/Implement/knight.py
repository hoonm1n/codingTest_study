cor = list(input())

x = ord(cor[0]) - ord("a") + 1
y = int(cor[1])

dx = [2, 2, 1, -1, -2, -2, 1, -1]
dy = [1, -1, -2, -2, 1, -1, 2, 2]

result = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<nx<9 and 0<ny<9:
        result += 1

print(result)