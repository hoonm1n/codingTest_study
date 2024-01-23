import sys
input = sys.stdin.readline

N = int(input())
map = [list(input()) for _ in range(N)]

def check():
    max = 0
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if map[i][j] == map[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            if max < cnt:
                max = cnt
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if map[j][i] == map[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            if max < cnt:
                max = cnt
    return max

result = 0
for i in range(N):
    for j in range(N-1):
        map[i][j], map[i][j+1] = map[i][j+1], map[i][j]
        k = check()
        if result < k:
            result = k
        map[i][j], map[i][j+1] = map[i][j+1], map[i][j]

for i in range(N):
    for j in range(N-1):
        map[j][i], map[j+1][i] = map[j+1][i], map[j][i]
        k = check()
        if result < k:
            result = k
        map[j][i], map[j+1][i] = map[j+1][i], map[j][i]

print(result)