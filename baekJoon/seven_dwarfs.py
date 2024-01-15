data = []
for i in range(9):
    k = int(input())
    data.append(k)

diff = sum(data) - 100
a = 0
b = 0
for i in range(9):
    for j in range(i+1, 9):
        if (data[i] + data[j]) == diff:
            a = data[i]
            b = data[j]
            break
data.remove(a)
data.remove(b)

data.sort()
for i in range(7):
    print(data[i], end = " ")