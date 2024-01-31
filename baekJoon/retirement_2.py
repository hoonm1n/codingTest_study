import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
schedule = []
day = [0] * (n+1)
for i in range(1, n+1):
    a, b = map(int, input().split())
    schedule.append((a,b))

for i in range(1, n+1):
    end_day = i + schedule[i-1][0] - 1
    if day[i] < day[i-1]:
        day[i] = day[i-1]
    if end_day < n+1:
        day[end_day] = max(day[end_day], day[i-1] + schedule[i-1][1])

print(day[n])