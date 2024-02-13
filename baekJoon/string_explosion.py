import sys
input = sys.stdin.readline

word = input().rstrip()
explode = input().rstrip()

stack = []
l = len(explode)

for i in range(len(word)):
    stack.append(word[i])
    if len(stack) >= l:
        if ''.join(stack[-l:]) == explode:
            for _ in range(l):
                stack.pop()

if len(stack) == 0:
    print("FRULA")  
else:
    print(''.join(stack))