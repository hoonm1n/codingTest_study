import itertools

n = int(input())
scv = list(map(int,input().split()))
while len(scv)<3:
    scv.append(0)
dp = [[[0]*(max(scv)+1) for _ in range(max(scv)+1)] for _ in range(max(scv)+1)]
dp[scv[0]][scv[1]][scv[2]] = 1

attack = list(itertools.permutations([1,3,9], 3))

for i in range(max(scv), -1, -1):
    for j in range(max(scv), -1, -1):
        for k in range(max(scv), -1, -1):
            if dp[i][j][k] > 0:
                for a in attack:
                    ni = i - a[0]
                    nj = j - a[1]
                    nk = k - a[2]
                    ni = max(0, ni)
                    nj = max(0, nj)
                    nk = max(0, nk)
                    if dp[ni][nj][nk] == 0 or dp[ni][nj][nk] > dp[i][j][k]+1:
                        dp[ni][nj][nk] = dp[i][j][k]+1

print(dp[0][0][0]-1)