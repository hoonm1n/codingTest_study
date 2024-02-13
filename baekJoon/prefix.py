import sys
input = sys.stdin.readline

n = int(input())
result = []
words = []
for i in range(n):
    words.append(input().rstrip())

for i in range(n):
    flag = 0
    for j in result:
        if j.startswith(words[i]):
            flag = 1
            break
        if words[i].startswith(j):
            flag = 1
            result.remove(j)
            result.append(words[i])
            break

    if flag == 0:
        result.append(words[i])

print(len(result))