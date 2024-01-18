def check():
    count = 0
    for w in word:
        for j in range(len(w)):
            if alpa[ord(w[j]) - ord('a')] == 0:
                break
            if j == len(w)-1 and alpa[ord(w[j]) - ord('a')] == 1:
                count += 1
    return count

def dfs(start, depth):
    global result
    if depth == K:
        result = max(result, check())
    for i in range(start, 26):
        if alpa[i] == 0:
            alpa[i] = 1
            dfs(i, depth +1)
            alpa[i] = 0

N, K = map(int, input().split())

word = []
alpa = [0] * 26
result = 0

for i in range(N):
    word.append(list(input()))
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    for i in {'a','n', 't', 'i', 'c'}:
        alpa[ord(i) - ord('a')] = 1
    dfs(0, 5)
    print(result)
