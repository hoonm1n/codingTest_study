import sys
input = sys.stdin.readline
import heapq
INF = 1e9

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
dp = [0]*(n+1)
for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    

def dijkstra(start):
    h = []
    distance[start] = 0
    heapq.heappush(h, (0, start))
    
    while h:
        now_dis, now = heapq.heappop(h)
        
        if distance[now] < now_dis:
            continue

        for g in graph[now]:
            if now_dis + g[0] < distance[g[1]]:
                distance[g[1]] = now_dis + g[0]
                heapq.heappush(h, (distance[g[1]], g[1]))


dijkstra(2)
dp[2] = 1
def ration_route(curr):
    if dp[curr] == 0:
        for next_dist, next in graph[curr]:
            if distance[curr] > distance[next]:
                dp[curr] += ration_route(next)
        return dp[curr]
    else:
        return dp[curr]


print(ration_route(1))
    

    
