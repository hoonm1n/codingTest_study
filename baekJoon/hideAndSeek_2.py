import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
vistied = [-1] * 100001
cnt = 0

def bfs(start):
    global cnt, vistied
    q = deque()
    q.append(start)
    vistied[start] = 0

    while q:
        now = q.popleft()
        if now == k:
            cnt += 1 

        for nx in [now+1, now*2, now-1]:
            if 0<= nx <100001:
                if vistied[nx] >= vistied[now] + 1 or vistied[nx] == -1:
                    vistied[nx] = vistied[now] + 1
                    q.append(nx)

bfs(n)
print(vistied[k])
print(cnt)

