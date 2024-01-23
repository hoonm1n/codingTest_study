import sys
input = sys.stdin.readline

S = int(input())
sum = 0
curr = 0
while sum <= S:
    curr += 1
    sum += curr

print(curr -1)