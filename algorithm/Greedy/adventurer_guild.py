n = int(input())
fearList = list(map(int, input().split()))
fearList.sort()

result = 0
count = 0

for i in fearList:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)
