n, k = map(int, input().split())

count = 0
table = [0] * (k+1)
array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)
table[0] = 1

for c in array:
    for i in range(c, k+1):
        table[i] += table[i - c]

print(table[k])