import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 


n = int(input())
p = [2,3,5,7]
curr = 0

def DFS(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            if is_prime_number(num*10 + i):
                DFS(num*10+i)

for k in p:
    DFS(k)
