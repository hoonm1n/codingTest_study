t = int(input())
result = []
for _ in range(t):
    n = int(input())
    table = [1] * (n+1)
    for i in range(2,n+1):
        table[i] += table[i-2]
    for i in range(3,n+1):
        table[i] += table[i-3]

    result.append(table[n])

for i in range(t):
    print(result[i])