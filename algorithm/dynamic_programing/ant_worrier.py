n = int(input())
array = list(map(int, input().split()))

d = [0]*n
d[0] = array[0]
if array[1] > array[0]:
    d[1] = array[1]
else:
    d[1] = array[0]

for i in range(2, n):
    if d[i-1] > d[i-2] + array[i]:
        d[i] = d[i-1]
    else:
        d[i] = d[i-2] + array[i]

print(d[n-1])
