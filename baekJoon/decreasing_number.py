import sys
from itertools import combinations

n = int(input())
nums = []

for i in range(1,11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        nums.append(int("".join(map(str, num))))
nums.sort()
if len(nums) <= n:
    print(-1)
else:
    print(nums[n])