a, b = map(int, input().split())
data = [0]
flag = False
for i in range(1, b+1):
    if flag == True:
        break
    for j in range(i):
        data.append(i)
        if len(data) > b:
            flag = True
            break

result = 0
for i in range(a, b+1):
    result += data[i]
print(result)