k = int(input())

for i in range(k):
    data = list(map(int, input().split()))
    data.sort()
    print(data[7])