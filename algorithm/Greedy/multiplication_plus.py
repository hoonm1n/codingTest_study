num = list(map(int, input()))
result = 0

for data in num:
  if (result <= 1):
    result += data
  elif (data == 0):
    pass
  else:
    result *= data

print(result)
