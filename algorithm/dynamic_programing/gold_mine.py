T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    data = []
    idx = 0
    for i in range(n):
        data.append(array[idx:idx+m])
        idx += m

    table = [[0]*m for _ in range(n)]
    
    for i in range(n):
        table[i][0] = data[i][0]
    
    for j in range(1, m):
        for i in range(n):
            if n == 1:
                table[i][j] = table[i-1][j-1] + data[i][j]
            elif 0 < i < n-1:
                table[i][j] = max(table[i-1][j-1], table[i][j-1], table[i+1][j-1]) + data[i][j]
            elif i == 0:
                table[i][j] = max(table[i][j-1], table[i+1][j-1]) + data[i][j]
            elif i == n-1:
                table[i][j] = max(table[i-1][j-1], table[i][j-1]) + data[i][j]
    result = 0
    for i in range(n):
        result = max(result, table[i][m-1])
    print(result)