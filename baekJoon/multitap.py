def find_lastest(idx):
    val = 0
    l_idx = -1
    for num in tap:
        try:
            t = elec[idx:].index(num)
        except:
            t = K+1
        if t > l_idx:
            val = num
            l_idx = t
    return val

N, K = map(int, input().split())
elec = list(map(int, input().split()))

tap = []
result = 0
for i in range(K):
    if elec[i] in tap:
        continue
    else:
        if len(tap) < N:
            tap.append(elec[i])
        else:
            result += 1
            last = find_lastest(i)
            tap.remove(last)
            tap.append(elec[i])

print(result)
