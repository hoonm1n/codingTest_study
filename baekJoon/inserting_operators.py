N = int(input())
data = list(map(int,input().split()))
op = list(map(int,input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, curr, plu, minus, mul, div):
    global maximum, minimum
    if depth == N:
        maximum = int(max(maximum, curr))
        minimum = int(min(minimum, curr))
        return
    if plu:
        dfs(depth+1, curr + data[depth], plu-1, minus, mul, div)
    if minus:
        dfs(depth+1, curr - data[depth], plu, minus-1, mul, div)
    if mul:
        dfs(depth+1, curr * data[depth], plu, minus, mul-1, div)
    if div:
        dfs(depth+1, int(curr / data[depth]), plu, minus, mul, div-1)

dfs(1, data[0], op[0], op[1], op[2], op[3])

print(maximum)
print(minimum)
    
    