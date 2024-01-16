def is_primeNum(n):
    if n < 3:
        if n == 2:
            return True
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

M = int(input())
N = int(input())

array = []

for i in range(M, N+1):
    if is_primeNum(i):
        array.append(i)

if len(array) < 1:
    print(-1)
else:
    print(sum(array))
    print(array[0])
