n = int(input())
array = list(map(int, input().split()))
array.reverse()

dt = [1]*n

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dt[i] = max(dt[i], dt[j] + 1)

print(n - max(dt))