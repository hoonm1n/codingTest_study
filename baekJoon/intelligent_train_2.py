station = []
for i in range(10):
    data = tuple(map(int, input().split()))
    station.append(data)

max = 0
curr = 0
for i in range(10):
    curr -= station[i][0]
    curr += station[i][1]
    if max < curr:
        max = curr
print(max)
