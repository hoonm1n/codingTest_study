n = int(input())
dt = [0]*(n+1)
if n != 0:
    dt[1] = 1
    for i in range(1, n+1):
        if dt[i] == 0:
            dt[i] = dt[i-1] + dt[i -2]
    print(dt[n])
else:
    print(0)