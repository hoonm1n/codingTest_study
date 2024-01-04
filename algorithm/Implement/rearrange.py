data = input()
alpa = []

k = 0

for i in data:
    if i.isalpha():
        alpa.append(i)
    else:
        k += int(i)
alpa.sort()
if k != 0:
    alpa.append(str(k))

print("".join(alpa))
