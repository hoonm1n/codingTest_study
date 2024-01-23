import heapq
import sys
input = sys.stdin.readline
INF = 1e9


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) 
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q) 

    if distance[now] < dist: 
      continue              

    for i in graph[now]:    
      if dist+i[1] < distance[i[0]]: 
        distance[i[0]] = dist+i[1]  
        heapq.heappush(q, (dist+i[1], i[0]))   

    
N = int(input())
M = int(input())
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start_node, des_node = map(int,input().split())
dijkstra(start_node)

print(distance[des_node])