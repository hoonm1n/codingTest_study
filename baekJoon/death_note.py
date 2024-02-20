import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
names = []
names.append(0)
for i in range(n):
    names.append(int(input()))

dp = [1e9] * (n+1)
dp[n] = 0

def note(index):
    if dp[index] < 1e9:
        return dp[index]
    remain = m - names[index] 
    for i in range(index+1, n+1):
        if remain >= 0:
            if i == n and remain >= names[i] + 1:
                dp[index] = 0
                break
            dp[index] = min(dp[index], remain*remain + note(i))
            remain -= (names[i]+1)
    return dp[index]    

note(1)
print(dp[1])