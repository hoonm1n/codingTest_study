a, b = map(int, input().split())
result = 1e9

def dfs(depth, curr):
    global result   
    if curr == b:
        result = min(result, depth)
        return
    if curr > b:
        return
    dfs(depth+1, curr * 2)
    dfs(depth+1, curr*10 + 1)
    
    return

dfs(1, a)
if result == 1e9:
    print(-1)
else:
    print(result)