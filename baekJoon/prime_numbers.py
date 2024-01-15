n = int(input())

data = list(map(int, input().split()))

result = 0
for i in range(n):
    k = 0
    if data[i] < 3:
        if data[i] == 1:
            result += 1
        continue
    for j in range(2, data[i]):
        if data[i] % j == 0:
            result += 1
            break

print(n - result)
