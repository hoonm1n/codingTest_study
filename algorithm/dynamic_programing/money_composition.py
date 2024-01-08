n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [0]*(m+1)

for i in range(1, m+1):
    d[i] = 10001
    if i < min(array):
        d[i] = -1
    else:
        for j in range(n):
            if i >= array[j]:
                if d[i-array[j]] != -1:
                    d[i] = min(d[i-array[j]] + 1, d[i])
            if j == n-1 and d[i] == 10001:
                d[i] = -1

print(d[m])