N, S = map(int, input().split())
data = list(map(int, input().split()))

tail = 0
sum = 0
min_length = N+1

for head in range(N):
    while sum < S and tail < N:
        sum += data[tail]
        tail += 1
    if sum >= S:
        min_length = min(tail-head, min_length)
    sum -= data[head]

if min_length == N+1:
    print(0)
else:
    print(min_length)