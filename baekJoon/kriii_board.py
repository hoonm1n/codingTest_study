n = int(input())

table = [i+1 for i in range(n)]

if n < 7:
    print(n)
else:
    for i in range(6, n):
        table[i] = max(table[i], table[i-3] * 2, table[i-4] * 3, table[i-5] * 4)

    print(max(table))