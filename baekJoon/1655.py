import sys
import heapq

input = sys.stdin.readline

n = int(input())

leftHeap = []
rightHeap = []

result = []

for i in range(1, n + 1):
  number = int(input())
  if len(leftHeap) == len(rightHeap):
    heapq.heappush(leftHeap, (-number, number))
  else:
    heapq.heappush(rightHeap, (number, number))

  if rightHeap and leftHeap[0][1] > rightHeap[0][1]:
    min = heapq.heappop(rightHeap)
    max = heapq.heappop(leftHeap)
    heapq.heappush(leftHeap, (-min[1], min[1]))
    heapq.heappush(rightHeap, (max[1], max[1]))

  result.append(leftHeap[0][1])

for i in result:
  print(i)
