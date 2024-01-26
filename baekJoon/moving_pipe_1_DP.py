N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

DP = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

DP[0][0][1] = 1
for i in range(2,N):
    if map[0][i] == 0:
        DP[0][0][i] = DP[0][0][i - 1]
    if map[0][i] == 1:
        break
for i in range(1,N):
    for j in range(1, N):
        if map[i][j] == 0 and map[i-1][j] == 0 and map[i][j-1] == 0:
            DP[2][i][j] = DP[2][i-1][j-1] + DP[1][i-1][j-1] + DP[0][i-1][j-1]
        
        if map[i][j] == 0:
            DP[0][i][j] = DP[0][i][j-1] + DP[2][i][j-1]
            DP[1][i][j] = DP[1][i-1][j] + DP[2][i-1][j]
 
print(DP[0][N-1][N-1] + DP[1][N-1][N-1] + DP[2][N-1][N-1])