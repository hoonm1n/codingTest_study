H, W = map(int, input().split())
block = list(map(int, input().split()))

map = [[0]*W for _ in range(H)]
for i in range(W):
    for j in range(H-1, H-1-block[i], -1):
        map[j][i] = 1

result = 0
for i in range(H):
    check = 501
    for j in range(W):
        if map[i][j] == 1:
            if check < j:
                result += (j-check-1)
                check = j
            else:
                check = j

print(result)