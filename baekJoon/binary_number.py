t = int(input())

for i in range(t):
    n = int(input())
    array = []
    z = 1
    while n != 0:
        z = n % 2
        n = int(n / 2)
        array.append(z)

    for i in range(len(array)):
        if array[i] == 1:
            print(i, end = ' ')
    
